slc.outdated
============

slc.outdated provides an object action for plone to toggle an
*outdated* flag on any object that is IAnnotatable. The value of the
flag is stored in an annotation, indexed in the catalog via an indexer
and included in the metadata.

By that you can use it for catalog queries and e.g. set CSS classes
accordingly.

A viewlet will appear below the title of outdated content, indicating
that this content is outdated. Further, the acquisition chain will be
consulted for "outdated_info" and if found, its title and text body
will be displayed. It should be published and hidden from the
navigation.

The software is tested manually and fully functional. The lack of
tests I consider a bug. I'd be most grateful if you donate tests, in
case you plan on using slc.outdated.
