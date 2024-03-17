"""Definition of meta model 'USchema'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'USchema'
nsURI = 'http://www.modelum.es/USchema'
nsPrefix = 'USchema'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class USchema(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    entities = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    relationships = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, entities=None, relationships=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if entities:
            self.entities.extend(entities)

        if relationships:
            self.relationships.extend(relationships)


class StructuralVariation(EObject, metaclass=MetaEClass):

    variationId = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    count = EAttribute(eType=ELong, unique=True, derived=False, changeable=True, default_value=0)
    firstTimestamp = EAttribute(eType=ELong, unique=True, derived=False, changeable=True)
    lastTimestamp = EAttribute(eType=ELong, unique=True, derived=False, changeable=True)
    features = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    container = EReference(ordered=True, unique=True, containment=False, derived=False)
    logicalFeatures = EReference(ordered=True, unique=True,
                                 containment=False, derived=False, upper=-1)
    structuralFeatures = EReference(ordered=True, unique=True,
                                    containment=False, derived=False, upper=-1)

    def __init__(self, *, variationId=None, features=None, count=None, firstTimestamp=None, lastTimestamp=None, container=None, logicalFeatures=None, structuralFeatures=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if variationId is not None:
            self.variationId = variationId

        if count is not None:
            self.count = count

        if firstTimestamp is not None:
            self.firstTimestamp = firstTimestamp

        if lastTimestamp is not None:
            self.lastTimestamp = lastTimestamp

        if features:
            self.features.extend(features)

        if container is not None:
            self.container = container

        if logicalFeatures:
            self.logicalFeatures.extend(logicalFeatures)

        if structuralFeatures:
            self.structuralFeatures.extend(structuralFeatures)


@abstract
class Feature(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


@abstract
class DataType(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class SchemaType(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    parents = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    variations = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, name=None, parents=None, variations=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if parents:
            self.parents.extend(parents)

        if variations:
            self.variations.extend(variations)


class EntityType(SchemaType):

    root = EAttribute(eType=EBoolean, unique=True, derived=False,
                      changeable=True, default_value=False)

    def __init__(self, *, root=None, **kwargs):

        super().__init__(**kwargs)

        if root is not None:
            self.root = root


class PList(DataType):

    elementType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, elementType=None, **kwargs):

        super().__init__(**kwargs)

        if elementType is not None:
            self.elementType = elementType


class PrimitiveType(DataType):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class Null(DataType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RelationshipType(SchemaType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PMap(DataType):

    keyType = EReference(ordered=True, unique=True, containment=True, derived=False)
    valueType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, keyType=None, valueType=None, **kwargs):

        super().__init__(**kwargs)

        if keyType is not None:
            self.keyType = keyType

        if valueType is not None:
            self.valueType = valueType


class PSet(DataType):

    elementType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, elementType=None, **kwargs):

        super().__init__(**kwargs)

        if elementType is not None:
            self.elementType = elementType


class PTuple(DataType):

    elements = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, elements=None, **kwargs):

        super().__init__(**kwargs)

        if elements:
            self.elements.extend(elements)


@abstract
class LogicalFeature(Feature):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class StructuralFeature(Feature):

    optional = EAttribute(eType=EBoolean, unique=True, derived=False,
                          changeable=True, default_value=False)

    def __init__(self, *, optional=None, **kwargs):

        super().__init__(**kwargs)

        if optional is not None:
            self.optional = optional


class Attribute(StructuralFeature):

    type = EReference(ordered=True, unique=True, containment=True, derived=False)
    key = EReference(ordered=True, unique=True, containment=False, derived=False)
    references = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, type=None, key=None, references=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if key is not None:
            self.key = key

        if references:
            self.references.extend(references)


class Reference(LogicalFeature):

    upperBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    lowerBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    opposite = EReference(ordered=True, unique=True, containment=False, derived=False)
    refsTo = EReference(ordered=True, unique=True, containment=False, derived=False)
    isFeaturedBy = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    attributes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, opposite=None, refsTo=None, isFeaturedBy=None, attributes=None, upperBound=None, lowerBound=None, **kwargs):

        super().__init__(**kwargs)

        if upperBound is not None:
            self.upperBound = upperBound

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if opposite is not None:
            self.opposite = opposite

        if refsTo is not None:
            self.refsTo = refsTo

        if isFeaturedBy:
            self.isFeaturedBy.extend(isFeaturedBy)

        if attributes:
            self.attributes.extend(attributes)


class Aggregate(StructuralFeature):

    upperBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    lowerBound = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    aggregates = EReference(ordered=True, unique=False, containment=False, derived=False, upper=-1)

    def __init__(self, *, aggregates=None, upperBound=None, lowerBound=None, **kwargs):

        super().__init__(**kwargs)

        if upperBound is not None:
            self.upperBound = upperBound

        if lowerBound is not None:
            self.lowerBound = lowerBound

        if aggregates:
            self.aggregates.extend(aggregates)


class Key(LogicalFeature):

    attributes = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, attributes=None, **kwargs):

        super().__init__(**kwargs)

        if attributes:
            self.attributes.extend(attributes)
