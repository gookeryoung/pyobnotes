# -*- encoding: utf-8 -*-

import os

from collections import namedtuple
from functools import partial

GetANSYSTemplate = partial(GetTemplate, Solver='ANSYS')
SystemInfo = namedtuple('SystemInfo', 'title position')

COMPONENT_GEOMETRY = 'Geometry'
COMPONENT_ENGINEERING_DATA = 'Engineering Data'
COMPONENT_MODEL = 'Model'
COMPONENT_SOLUTION = 'Solution'

TEMPLATE_TRANSIENT = 'SimulationSetupCellTemplate_ThermalTransientANSYS'
TEMPLATE_STEADY_STATE = 'SimulationSetupCellTemplate_ThermalSteadyStateANSYS'

MATERIAL_STEEL = 'Structural Steel'


class AbstractSimSystem(object):
    TEMPLATE_NAME = ''
    TEMPLATE_COMPONENT = ''
    TEMPLATE_MATERIAL = ''

    def __init__(self, name, title, relative=None, position='Right'):
        self.name = name
        self.title = title
        self.relative = relative
        self.position = position

        self.system = self.load_system()

        if self.TEMPLATE_MATERIAL:
            self.load_material()

    def load_system(self):
        for system in GetAllSystems():
            if system.Name == self.name:
                loaded = GetSystem(Name=self.name)
                return loaded

        return self.load_from_template()

    @property
    def components(self):
        if not self.relative:
            msg = u'未设置关联系统，创建系统[{}]-[{}]失败'.format(self.name, self.title)
            Ansys.UI.Toolkit.MessageBox.Show(msg)
            return None, None, None, None

        eng = self.relative.GetComponent(Name=COMPONENT_ENGINEERING_DATA)
        geometry = self.relative.GetComponent(Name=COMPONENT_GEOMETRY)
        model = self.relative.GetComponent(Name=COMPONENT_MODEL)
        solution = self.relative.GetComponent(Name=COMPONENT_SOLUTION)
        return eng, geometry, model, solution

    def __repr__(self):
        return u'Template={}, name={}, title={}'.format(self.TEMPLATE_NAME, self.name, self.title)

    def __str__(self):
        return u'System: {}, {}'.format(self.name, self.title)

class TransferNoneTemplateMixin(object):
    def load_from_template(self):
        template = GetTemplate(TemplateName=self.TEMPLATE_NAME)
        loaded = template.CreateSystem(Name=self.name)
        loaded.DisplayText = self.title
        return loaded

class LoadMaterialTemplateMixin(object):
    def load_material(self):
        container_eng = self.system.GetContainer(ComponentName=COMPONENT_ENGINEERING_DATA)
        for mat in container_eng.GetMaterials():
            mat.Delete()

        container_eng.Import(Source=self.TEMPLATE_MATERIAL)


class GeometrySystem(AbstractSimSystem, TransferNoneTemplateMixin):
    TEMPLATE_NAME = 'Geometry'


class TransferGeometryTemplateMixin(object):
    def load_from_template(self):
        template = GetANSYSTemplate(TemplateName=self.TEMPLATE_NAME)
        geometry = self.relative.GetComponent(Name=COMPONENT_GEOMETRY)
        loaded = template.CreateSystem(Name=self.name, ComponentsToShare=[geometry],
                                       Position=self.position, RelativeTo=self.relative)
        loaded.DisplayText = self.title
        return loaded


class TransferModelTemplateMixin(object):
    def load_from_template(self):
        template = GetANSYSTemplate(TemplateName=self.TEMPLATE_NAME)
        eng, geometry, model, solu = self.components
        loaded = template.CreateSystem(Name=self.name,
                                       ComponentsToShare=[eng, geometry, model],
                                       Position=self.position,
                                       RelativeTo=self.relative)
        loaded.DisplayText = self.title
        return loaded


class ElectricShareGeometrySystem(AbstractSimSystem, TransferGeometryTemplateMixin):
    TEMPLATE_NAME = 'Electric'

class ElectricShareGeometryMaterialSystem(AbstractSimSystem, TransferGeometryTemplateMixin, LoadMaterialTemplateMixin):
    TEMPLATE_NAME = 'Electric'
    TEMPLATE_MATERIAL = os.path.join(os.path.dirname(__file__), 'materials', 'materials_metalfilm.xml')

class ElectricShareModelSystem(AbstractSimSystem, TransferModelTemplateMixin):
    TEMPLATE_NAME = 'Electric'


class TransferSolutionTemplateMixin(object):
    def load_from_template(self):
        template = GetANSYSTemplate(TemplateName=self.TEMPLATE_NAME)
        eng, geometry, model, solu = self.components
        if all([eng, geometry, model, solu]):
            component = GetComponentTemplate(Name=self.TEMPLATE_COMPONENT)
            transfer = Set(FromComponent=solu, TransferName=None, ToComponentTemplate=component)
            loaded = template.CreateSystem(Name=self.name,
                                           ComponentsToShare=[eng, geometry, model],
                                           DataTransferFrom=[transfer],
                                           Position=self.position,
                                           RelativeTo=self.relative)
            loaded.DisplayText = self.title
            return loaded
        else:
            return None


class TransientThermalSystem(AbstractSimSystem, TransferSolutionTemplateMixin):
    TEMPLATE_NAME = 'Transient Thermal'
    TEMPLATE_COMPONENT = TEMPLATE_TRANSIENT


class SteadyStateThermalSystem(AbstractSimSystem, TransferSolutionTemplateMixin):
    TEMPLATE_NAME = 'Steady-State Thermal'
    TEMPLATE_COMPONENT = TEMPLATE_STEADY_STATE

