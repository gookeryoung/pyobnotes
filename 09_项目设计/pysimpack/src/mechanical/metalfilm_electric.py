# -*- encoding: utf-8 -*-

def set_material(location, material):
    assign = Model.Materials.AddMaterialAssignment()
    assign.Location = location
    assign.Material = material

def set_coordinate(location, name):
    coord = Model.CoordinateSystems.AddCoordinateSystem()
    coord.Name = name
    coord.OriginLocation = location

def set_mesh_by_esize(location, size):
    mesh = Model.Mesh.AddSizing()
    mesh.Type = SizingType.ElementSize
    mesh.ElementSize = Quantity('{}[mm]'.format(size))
    mesh.Location = location

def set_mesh_by_influence(location, size, center, radius):
    mesh = Model.Mesh.AddSizing()
    mesh.Type = SizingType.SphereOfInfluence
    mesh.Location = location
    mesh.ElementSize = Quantity('{}[mm]'.format(size))
    mesh.SphereCenter = center
    mesh.SphereRadius = Quantity('{}[mm]'.format(radius))

def main():
    dic_ns = {x.Name: x for x in Model.NamedSelections.Children}
    dic_mt = {x.Name: x for x in Model.Materials.Children}
    dic_sl = {x.Name: x for x in Model.Analyses}

    # 设置模型材料
    material_assign = {
        'NSV_FILM': 'Nickel alloy, Nichrome V, annealed',
        'NSV_PIN': 'Copper Alloy',
        'NSV_BASE': 'Alumina 96%'
    }
    for k, v in material_assign.items():
        set_material(dic_ns[k], v)

    # 设置桥区中心坐标系
    set_coordinate(dic_ns['NSL_FILM_BRIDGE'], 'Center')

    # 设置网格划分
    set_mesh_by_esize(dic_ns['NSV_BASE&PIN'], 0.2)
    set_mesh_by_esize(dic_ns['NSF_FILM_TOP'], 0.1)
    set_mesh_by_influence(dic_ns['NSF_FILM_TOP'], 0.02, Model.CoordinateSystems.Children[1], 1.0)

    # 设置边界条件
    ssec = dic_sl['Steady-State Electric Conduction']
    vol = ssec.AddVoltage()
    vol.Location = dic_ns['NSF_VOL']
    vol.Magnitude.Output.DiscreteValues=[Quantity('0 [V]')]

    cur = ssec.AddCurrent()
    cur.Location = dic_ns['NSF_CUR']
    cur.Magnitude.Output.DiscreteValues = [Quantity('1.0[A]')]

    ssec.Solution.AddElectricVoltage()
    Model.Mesh.GenerateMesh()
    ssec.Solve()

main()
