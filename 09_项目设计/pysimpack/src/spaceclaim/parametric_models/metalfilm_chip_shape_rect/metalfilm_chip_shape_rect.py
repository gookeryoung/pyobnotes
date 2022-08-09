# Python Script For SpaceClaim, API Version = V19
ClearAll()

import math

from collections import namedtuple

PartParameter = namedtuple('PartParameter', 'desc value')

PS = {
    # 基座相关参数
    'BT': PartParameter(u'基座厚度(base thickness)', Parameters.BT),
    'BL': PartParameter(u'基座长度(base length)', Parameters.BL),
    'BW': PartParameter(u'基座宽度(base width)', Parameters.BW),
    'BTD': PartParameter(u'基座过孔直径(base through diameter)', Parameters.BTD),
    'BTW': PartParameter(u'基座过孔间距(base through width)', Parameters.BTW),

    # 桥区/薄膜相关参数
    'FT': PartParameter(u'薄膜厚度(film thickness)', Parameters.FT),
    'FBL': PartParameter(u'薄膜桥区长度(film bridge length)', Parameters.FBL),
    'FBW': PartParameter(u'薄膜桥区宽度(film bridge width)', Parameters.FBW),
    'FBA': PartParameter(u'薄膜桥区夹角(film bridge angle)', Parameters.FBA),
}

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

def extrude_faces(faces, length):
    options = ExtrudeFaceOptions(ExtrudeType=ExtrudeType.None)
    selection = Selection.Create(*faces)
    ExtrudeFaces.Execute(selection, length, options)

def create_base_component(bt, bl, bw, btd, btw):
    """建立基座模型, 相关参数: BT/BL/BW/BTD/BTW"""
    ViewHelper.SetSketchPlane(Plane.PlaneXY, None)
    SketchHelper.StartConstraintSketching()

    # 构造外形草图
    corners = ((-bl / 2, bw / 2), (-bl / 2, -bw / 2), (bl / 2, -bw / 2))
    SketchRectangle.Create(*(Point2D.Create(MM(x), MM(y)) for x, y in corners))

    # 构造填料孔草图
    SketchCircle.Create(Point2D.Create(MM(-btw / 2), MM(0)), MM(btd / 2))
    SketchCircle.Create(Point2D.Create(MM(btw / 2), MM(0)), MM(btd / 2))

    # 拉伸实体
    ViewHelper.SetViewMode(InteractionMode.Solid)
    extrude_faces([GetRootPart().Bodies[0].Faces[2]], MM(-bt))
    Delete.Execute(BodySelection.Create(GetRootPart().Bodies[0]))

    # 建立组件
    base_comp = set_body_component(GetRootPart().Bodies[0], 'base')
    return base_comp

def create_fill_component(bt, btd, btw):
    """建立填料模型, 相关参数: BTD/BTW/BT"""
    ViewHelper.SetSketchPlane(Plane.PlaneXY, None)
    SketchHelper.StartConstraintSketching()

    # 构造外形草图
    SketchCircle.Create(Point2D.Create(MM(-btw / 2), MM(0)), MM(btd / 2))
    SketchCircle.Create(Point2D.Create(MM(btw / 2), MM(0)), MM(btd / 2))

    # 拉伸实体
    ViewHelper.SetViewMode(InteractionMode.Solid)
    extrude_faces([GetRootPart().Bodies[0].Faces[i] for i in range(2)], MM(-bt))

    # 建立组件
    fill_comp = ComponentHelper.CreateAtRoot('fill')
    move_to_component(GetRootPart().Bodies[0], 'fill1', fill_comp)
    move_to_component(GetRootPart().Bodies[0], 'fill2', fill_comp)

    # 设置填料颜色
    sel = Selection.Create(fill_comp)
    ColorHelper.SetColor(sel, SetColorOptions(), Color.FromArgb(120, 255, 120, 64))
    return fill_comp

def create_film_component(bl, bw, ft, fbl, fbw, fba):
    """建立桥区模型, 相关参数: BL/BW/FT/FBL/FBW/FBA"""
    ViewHelper.SetSketchPlane(Plane.PlaneXY, None)
    SketchHelper.StartConstraintSketching()

    # 构造外形草图
    corners = ((-bl / 2, bw / 2), (-bl / 2, -bw / 2), (bl / 2, -bw / 2))
    SketchRectangle.Create(*[Point2D.Create(MM(x), MM(y)) for x, y in corners])

    # 构造桥区草图
    corners = ((-fbl / 2, fbw / 2), (-fbl / 2, -fbw / 2), (fbl / 2, fbw / 2), (fbl / 2, -fbw / 2))
    lt, lb, rt, rb = (Point2D.Create(MM(x), MM(y)) for x, y in corners)
    SketchLine.Create(lt, rt)
    SketchLine.Create(lb, rb)
    dx = (bw - fbw) / 2 * math.tan(fba / 180.0 * math.pi)
    SketchLine.Create(lt, Point2D.Create(MM(-fbl / 2 - dx), MM(bw / 2)))
    SketchLine.Create(rt, Point2D.Create(MM(fbl / 2 + dx), MM(bw / 2)))
    SketchLine.Create(lb, Point2D.Create(MM(-fbl / 2 - dx), MM(-bw / 2)))
    SketchLine.Create(rb, Point2D.Create(MM(fbl / 2 + dx), MM(-bw / 2)))

    # 拉伸实体
    ViewHelper.SetViewMode(InteractionMode.Solid)
    extrude_faces([GetRootPart().Bodies[0].Faces[2]], MM(ft))
    Delete.Execute(BodySelection.Create(GetRootPart().Bodies[0]))

    # 建立组件
    film_comp = set_body_component(GetRootPart().Bodies[0], 'film')

    # 设置填料颜色
    sel = Selection.Create(film_comp)
    ColorHelper.SetColor(sel, SetColorOptions(), Color.FromArgb(255, 128, 255, 255))
    return film_comp

def main():
    for k, v in PS.items():
        print u'参数: {:<3}\t| 描述: {:<40}\t| 值: {:<5f}'.format(k, v.desc, v.value)

    # 建立模型
    base_comp = create_base_component(*(x.value for x in (PS['BT'], PS['BL'], PS['BW'], PS['BTD'], PS['BTW'])))
    fill_comp = create_fill_component(*(x.value for x in (PS['BT'], PS['BTD'], PS['BTW'])))
    film_comp = create_film_component(*(x.value for x in (PS['BL'], PS['BW'], PS['FT'], PS['FBL'], PS['FBW'], PS['FBA'])))

    # 建立NS
    set_named_selection([base_comp.Content.Bodies[0]], 'NSV_BASE')
    set_named_selection([base_comp.Content.Bodies[0].Faces[i] for i in range(4)], 'NSF_BASE_CYLINDER')

    set_named_selection([fill_comp.Content.Bodies[i] for i in range(2)], 'NSV_FILL')
    set_named_selection([fill_comp.Content.Bodies[0].Faces[1]], 'NSF_CUR')
    set_named_selection([fill_comp.Content.Bodies[1].Faces[1]], 'NSF_VOL')
    set_named_selection([base_comp.Content.Bodies[0], fill_comp.Content.Bodies[0], fill_comp.Content.Bodies[1]], 'NSV_BASE&FILL')
    
    set_named_selection([film_comp.Content.Bodies[0]], 'NSV_FILM')
    set_named_selection([film_comp.Content.Bodies[0].Edges[4], film_comp.Content.Bodies[0].Edges[22]], 'NSL_BRIDGE')
    set_named_selection([film_comp.Content.Bodies[0].Faces[12]], 'NSF_FILM_TOP')

main()
