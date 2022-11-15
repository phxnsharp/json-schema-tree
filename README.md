Example of creating a [JSON-Schema](https://json-schema.org) that defines a simple tree document. 

The tree can have two types of leaf nodes (LeafA and LeafB), and two types of containers 
(ContainerA and ContainerB).

This is implemented by using an `allOf` constraint to represent the object hierarchy, and a
disambiguator `oneOf` definition to allow one of the 4 types at any location in the tree. 

Using the [jschon](https://github.com/marksparkza/jschon) Python implementation I tested this
schema. For a simple instance with 4 nodes that is invalid in a minor way (typo), it generates
[370 lines of largely incomprehensible error messages](result.err). 

The question is, how could this be implemented in a way that would produce better error
messages?
