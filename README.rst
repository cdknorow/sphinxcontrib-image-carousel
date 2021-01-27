image-carousel
===============

Easy Image Carousels in Sphinx documentation (focused on HTML).


Features
--------

* Show Multiple Images in a Carousel (HTML).


How to install?
---------------

copy the Contents of the sphinxcontrib Folder to your project

cd sphinxcontrib
cp -r _static ext <Path-To-Your-Project>

add extension to ``conf.py`` in your Sphinx project. ::


    sys.path.append(os.path.abspath("./ext"))


    extensions = [
              …
              'image_carousel',
              …
              ]


How to use it?
--------------

Example: ::

    .. imagecarousel:: picture.png, caption image 1,picture2.png, capture picture 2, picture3.png, caption picture3

