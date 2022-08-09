
# Python Script For SpaceClaim, API Version = V19
ClearAll()

from collections import namedtuple

PartParameter = namedtuple('PartParameter', 'desc value')

PS = {
    # 基座相关参数
    'BT': PartParameter(u'基座厚度(base thickness)', Parameters.BT),
    'BD': PartParameter(u'基座直径(base diameter)', Parameters.BD),
    'BTD': PartParameter(u'基座过孔直径(base through diameter)', Parameters.BTD),
    'BTW': PartParameter(u'基座过孔间距(base through width)', Parameters.BTW),
    
    # 极针相关参数
    'PL': PartParameter(u'极针长度(pin length)', Parameters.PL),

    # 桥区/薄膜相关参数
    'FT': PartParameter(u'薄膜厚度(film thickness)', Parameters.FT),
    'FD': PartParameter(u'薄膜直径(film diameter)', Parameters.FD),
    'FBL': PartParameter(u'薄膜桥区长度(film bridge length)', Parameters.FBL),
    'FBW': PartParameter(u'薄膜桥区宽度(film bridge width)', Parameters.FBW),
    'FBA': PartParameter(u'薄膜桥区夹角(film bridge angle)', Parameters.FBA),
}

SEL = Selection.Create

def set_body_component(body, comp_name):
    component = ComponentHelper.CreateAtRoot(comp_name)
    move_to_component(body, comp_name, component)
    return component

def move_to_component(body, name, comp):
    sel = BodySelection.Create(body)
    RenameObject.Execute(sel, name)
    ComponentHelper.MoveBodiesToComponent(sel, comp, False)

def set_named_selection(parts, name):
    primary = Selection.CreateByObjects(parts)
    NamedSelection.Create(primary, Selection.Empty())
    NamedSelection.Rename("组1", name)

def set_coincident(src, dst):
    sel_src = SelectionPoint.Create(*src)
    sel_dst = SelectionPoint.Create(*dst)
    Constraint.CreateCoincident(sel_src, sel_dst)

def set_dimension_angle(src, dst, value):
    sel_src = Selection.Create(src)
    sel_dst = Selection.Create(dst)
    Dimension.CreateAngle(sel_src, sel_dst)

def extrude_faces(faces, length):
    options = ExtrudeFaceOptions(ExtrudeType=ExtrudeType.None)
    selection = Selection.Create(*faces)
    ExtrudeFaces.Execute(selection, length, options)

def create_base_component(bt, bd, btd, btw):
    """建立基座模型, 相关参数: BT/BD/BTD/BTW"""
    ViewHelper.SetSketchPlane(Plane.PlaneXY, None)
    SketchHelper.StartConstraintSketching()

    # 构造外形草图
    SketchCircle.Create(Point2D.Create(MM(0), MM(0)), MM(bd / 2))

    # 构造填料孔草图
    SketchCircle.Create(Point2D.Create(MM(-btw / 2), MM(0)), MM(btd / 2))
    SketchCircle.Create(Point2D.Create(MM(btw / 2), MM(0)), MM(btd / 2))

    # 拉伸实体
    ViewHelper.SetViewMode(InteractionMode.Solid)
    extrude_faces([GetRootPart().Bodies[0].Faces[2]], MM(-bt))
    Delete.Execute(BodySelection.Create(GetRootPart().Bodies[0]))

    # 建立组件
    return set_body_component(GetRootPart().Bodies[0], 'base')

def create_pin_component(pl, btd, btw):
    """建立极针模型, 相关参数: PL/BTD/BTW"""
    ViewHelper.SetSketchPlane(Plane.PlaneXY, None)
    SketchHelper.StartConstraintSketching()

    # 构造外形草图
    SketchCircle.Create(Point2D.Create(MM(-btw / 2), MM(0)), MM(btd / 2))
    SketchCircle.Create(Point2D.Create(MM(btw / 2), MM(0)), MM(btd / 2))

    # 拉伸实体
    ViewHelper.SetViewMode(InteractionMode.Solid)
    extrude_faces([GetRootPart().Bodies[0].Faces[i] for i in range(2)], MM(-pl))

    # 建立组件
    pin_comp = ComponentHelper.CreateAtRoot('pin')
    move_to_component(GetRootPart().Bodies[0], 'pin1', pin_comp)
    move_to_component(GetRootPart().Bodies[0], 'pin2', pin_comp)

    # 设置填料颜色
    ColorHelper.SetColor(Selection.Create(pin_comp), SetColorOptions(), Color.FromArgb(120, 255, 120, 64))
    return pin_comp

def create_film_component(ft, fd, fbl, fbw, fba):
    """建立桥区模型, 相关参数: BD/FT/FBL/FBW/FBA"""
    ViewHelper.SetSketchPlane(Plane.PlaneXY, None)
    SketchHelper.StartConstraintSketching()
    plane = GetRootPart().DatumPlanes[0]

    # 构造外形草图
    SketchCircle.Create(Point2D.Create(MM(0), MM(0)), MM(fd / 2)) # Curve[0]

    # 构造桥区草图
    corners = ((-fbl / 2, fbw / 2), (-fbl / 2, -fbw / 2), (fbl / 2, fbw / 2), (fbl / 2, -fbw / 2))
    lt, lb, rt, rb = (Point2D.Create(MM(x), MM(y)) for x, y in corners)
    SketchLine.Create(lt, rt) # Curve[1]
    SketchLine.Create(lb, rb) # Curve[2]
    map(Constraint.CreateFixed, [Selection.Create(plane.Curves[i]) for i in range(3)])

    SketchLine.Create(rt, Point2D.Create(MM(fbl/2), MM(fd/2))) # Curve[3]
    set_coincident(src=(plane.Curves[3].GetChildren[ICurvePoint]()[1],), dst=(plane.Curves[0],))
    set_coincident(src=(plane.Curves[3].GetChildren[ICurvePoint]()[0],), dst=(plane.Curves[1].GetChildren[ICurvePoint]()[1],))
    Dimension.CreateAngle(SEL(plane.Curves[3]), SEL(plane.Curves[1]), True, DEG(90+fba))
    
    SketchLine.Create(lt, Point2D.Create(MM(-fbl/2), MM(fd/2))) # Curve[4]
    set_coincident(src=(plane.Curves[4].GetChildren[ICurvePoint]()[1],), dst=(plane.Curves[0],))
    set_coincident(src=(plane.Curves[4].GetChildren[ICurvePoint]()[0],), dst=(plane.Curves[1].GetChildren[ICurvePoint]()[0],))
    Dimension.CreateAngle(SEL(plane.Curves[4]), SEL(plane.Curves[1]), True, DEG(90-fba))
    
    SketchLine.Create(rb, Point2D.Create(MM(fbl/2), MM(-fd/2))) # Curve[5]
    set_coincident(src=(plane.Curves[5].GetChildren[ICurvePoint]()[1],), dst=(plane.Curves[0],))
    set_coincident(src=(plane.Curves[5].GetChildren[ICurvePoint]()[0],), dst=(plane.Curves[2].GetChildren[ICurvePoint]()[1],))
    Dimension.CreateAngle(SEL(plane.Curves[5]), SEL(plane.Curves[2]), True, DEG(90+fba))
    
    SketchLine.Create(lb, Point2D.Create(MM(-fbl/2), MM(-fd/2))) # Curve[6]
    set_coincident(src=(plane.Curves[6].GetChildren[ICurvePoint]()[1],), dst=(plane.Curves[0],))
    set_coincident(src=(plane.Curves[6].GetChildren[ICurvePoint]()[0],), dst=(plane.Curves[2].GetChildren[ICurvePoint]()[0],))
    Dimension.CreateAngle(SEL(plane.Curves[6]), SEL(plane.Curves[2]), True, DEG(90-fba))

    # 拉伸实体
    ViewHelper.SetViewMode(InteractionMode.Solid, None)
    extrude_faces([GetRootPart().Bodies[0].Faces[1]], MM(ft))
    Delete.Execute(BodySelection.Create(GetRootPart().Bodies[0]))

    # 建立组件
    film_comp = set_body_component([GetRootPart().Bodies[0]], 'film')
    ColorHelper.SetColor(Selection.Create(film_comp), SetColorOptions(), Color.FromArgb(255, 0, 128, 255))
    return film_comp

def main():
    for k, v in PS.items():
        print u'参数: {:<3}\t| 描述: {:<40}\t| 值: {:<5f}'.format(k, v.desc, v.value)

    # 建立模型
    base_comp = create_base_component(*(x.value for x in (PS['BT'], PS['BD'], PS['BTD'], PS['BTW'])))
    pin_comp = create_pin_component(*(x.value for x in (PS['PL'], PS['BTD'], PS['BTW'])))
    film_comp = create_film_component(*(x.value for x in (PS['FT'], PS['FD'], PS['FBL'], PS['FBW'], PS['FBA'])))

    # 建立NS
    set_named_selection([base_comp.Content.Bodies[0]], 'NSV_BASE')
    set_named_selection([base_comp.Content.Bodies[0].Faces[0]], 'NSF_BASE_CYLINDER')
    
    set_named_selection([pin_comp.Content.Bodies[i] for i in range(2)], 'NSV_PIN')
    set_named_selection([pin_comp.Content.Bodies[0].Faces[1]], 'NSF_CUR')
    set_named_selection([pin_comp.Content.Bodies[1].Faces[1]], 'NSF_VOL')
    set_named_selection([base_comp.Content.Bodies[0], pin_comp.Content.Bodies[0], pin_comp.Content.Bodies[1]], 'NSV_BASE&PIN')

    set_named_selection([film_comp.Content.Bodies[0]], 'NSV_FILM')
    set_named_selection([film_comp.Content.Bodies[0].Faces[8]], 'NSF_FILM_TOP')
    set_named_selection([film_comp.Content.Bodies[0].Edges[0], film_comp.Content.Bodies[0].Edges[13]], 'NSL_FILM_BRIDGE')

main()
