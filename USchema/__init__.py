
from .USchema import getEClassifier, eClassifiers
from .USchema import name, nsURI, nsPrefix, eClass
from .USchema import USchema, EntityType, StructuralVariation, Feature, Attribute, DataType, PList, Reference, Aggregate, PrimitiveType, Null, RelationshipType, SchemaType, PMap, PSet, PTuple, LogicalFeature, Key, StructuralFeature


from . import USchema

__all__ = ['USchema', 'EntityType', 'StructuralVariation', 'Feature', 'Attribute', 'DataType', 'PList', 'Reference', 'Aggregate',
           'PrimitiveType', 'Null', 'RelationshipType', 'SchemaType', 'PMap', 'PSet', 'PTuple', 'LogicalFeature', 'Key', 'StructuralFeature']

eSubpackages = []
eSuperPackage = None
USchema.eSubpackages = eSubpackages
USchema.eSuperPackage = eSuperPackage

USchema.entities.eType = EntityType
USchema.relationships.eType = RelationshipType
StructuralVariation.features.eType = Feature
StructuralVariation.logicalFeatures.eType = LogicalFeature
StructuralVariation.structuralFeatures.eType = StructuralFeature
Attribute.type.eType = DataType
PList.elementType.eType = DataType
Reference.opposite.eType = Reference
Reference.refsTo.eType = EntityType
Reference.isFeaturedBy.eType = StructuralVariation
Aggregate.aggregates.eType = StructuralVariation
SchemaType.parents.eType = SchemaType
PMap.keyType.eType = PrimitiveType
PMap.valueType.eType = DataType
PSet.elementType.eType = DataType
PTuple.elements.eType = DataType
StructuralVariation.container.eType = SchemaType
Attribute.key.eType = Key
Attribute.references.eType = Reference
Reference.attributes.eType = Attribute
Reference.attributes.eOpposite = Attribute.references
SchemaType.variations.eType = StructuralVariation
SchemaType.variations.eOpposite = StructuralVariation.container
Key.attributes.eType = Attribute
Key.attributes.eOpposite = Attribute.key

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
