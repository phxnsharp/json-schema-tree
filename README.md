Example of creating a [JSON-Schema](https://json-schema.org) that defines a simple tree document. 

The tree can have two types of leaf nodes (LeafA and LeafB), and two types of containers 
(ContainerA and ContainerB).

On main this is implemented by using an `allOf` constraint to represent the object hierarchy, and a
disambiguator `oneOf` definition to allow one of the 4 types at any location in the tree. 

On [oneOf-anyOf](https://github.com/phxnsharp/json-schema-tree/tree/oneOf-anyOf) this is implemented
using a tricky nested structure of oneOf and anyOf keywords.

On [use-if](https://github.com/phxnsharp/json-schema-tree/tree/use-if) this is implemented 
using allOf and if statements. 

Using the [jschon](https://github.com/marksparkza/jschon) Python implementation I tested these
schemas. For a simple instance with 4 nodes that is invalid in a minor way (typo), it generates


- [main: 379 lines of largely incomprehensible error messages](https://github.com/phxnsharp/json-schema-tree/blob/main/result.err). 
- [oneOf-anyOf: 716 lines of largely incomprehensible error messages](https://github.com/phxnsharp/json-schema-tree/blob/oneOf-anyOf/result.err). 
- [use-if: 46 lines of slightly less incomprehensible error messages](https://github.com/phxnsharp/json-schema-tree/blob/use-if/result.err). 

The question is, how could this be implemented in a way that would produce better error
messages?

The [draft-next `propertyDependencies` keyword](https://github.com/orgs/json-schema-org/discussions/202) promises to help,
but does not quite completely alleviate it. On the [draft-next branch](https://github.com/phxnsharp/json-schema-tree/tree/draft-next)
you can see what the schema might look like. Issues I had:
 - I still have to write a qualifier before the `propertyDependencies` to ensure that the object is one of the proposed types and not 
   something completely different. `propertyDependencies` currently succeeds if none of the branches are chosen.
 - I want my tree to also have the ability to use a `{ "$ref":... }` object instead of one of the proposed types. In order to do
   so I have to fall back on the old, noisy, `*Of` blocks, or use a complex `if\then\else` statement.
