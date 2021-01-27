from docutils import nodes
import os
from docutils.parsers.rst import Directive
import posixpath
import shutil
from sphinx.util.osutil import ensuredir


def get_slide_info(self, code, options, prefix="image-carousel"):
    """
    Get path of output file.
    """
    content = code.split(",")
    filenames = []
    captions = []
    print("content")
    print(content)
    for i in range(0, len(content), 2):
        filenames.append(content[i].rstrip().lstrip())
        captions.append(content[i + 1].rstrip().lstrip())

    # HTML
    relfns = [posixpath.join(self.builder.imgpath, fname) for fname in filenames]
    outfns = [
        os.path.join(self.builder.outdir, "_images", fname) for fname in filenames
    ]

    for relfn, outfn in zip(relfns, outfns):
        ensuredir(os.path.dirname(outfn))
        print(relfn, outfn)
        shutil.copy(relfn, os.path.dirname(outfn))

    return list(zip(relfns, outfns, captions))


def create_image_carousel(carousel_index, slides):

    class_name = "slides-{}".format(carousel_index)
    dot_name = "dots-{}".format(carousel_index)

    html_output = ""
    total_slides = len(slides)

    def gen_slide(index, name, text):
        return """
            <div class="image-carousel-slides image-carousel-{class_name} fade">
                <div class="image-carousel-numbertext">{index} / {total_slides}</div>
                <img src="{image_name}" style="width:100%">
                <div class="image-carousel-text">{text_description}</div>
            </div>
            """.format(
            class_name=class_name,
            index=index,
            total_slides=total_slides,
            image_name=name,
            text_description=text,
        )

    for index, (relfn, _, text) in enumerate(slides):
        html_output += gen_slide(index, relfn, text)

    html_output += """<a class="image-carousel-prev" onclick="plusSlides({carousel_index}, -1)">&#10094;</a>
                      <a class="image-carousel-next" onclick="plusSlides({carousel_index}, 1)">&#10095;</a>
                    </div>
                    </br>
                    <div style="text-align:center">
        """.format(
        carousel_index=carousel_index
    )

    for index, _ in enumerate(slides):
        html_output += """<span class="image-carousel-dot image-carousel-{dot_name}" onclick="currentSlide({carousel_index}, {index})"></span>""".format(
            carousel_index=carousel_index, dot_name=dot_name, index=index
        )

    script = "<script>  var slideIndex = {{{}}};".format(
        ",".join("{}:{}".format(x, x) for x in range(carousel_index + 1))
    ) + "showSlides({carousel_index}); </script> ".format(carousel_index=carousel_index)

    return html_output + script


def render_dot_html(self, node, code, options, imgcls=None, alt=None):

    carousel_index = options["carousel_index"]

    slides = get_slide_info(self, code[0], options)

    self.body.append(self.starttag(node, "div", CLASS="image-carousel-container"))

    self.body.append(create_image_carousel(carousel_index, slides))

    self.body.append("</div>\n")

    raise nodes.SkipNode


def html_visit_image_carousel(self, node):
    render_dot_html(self, node, node["code"], node["options"])


class image_carousel(nodes.General, nodes.Element):
    pass


class ImageCarousel(Directive):
    has_content = True

    def run(self):
        dotcode = self.content

        env = self.state.document.settings.env

        if not hasattr(env, "all_image_carousels"):
            env.all_image_carousels = {}
            if not hasattr(env.all_image_carousels, env.docname):
                env.all_image_carousels[env.docname] = []

        node = image_carousel()
        node["code"] = dotcode
        node["options"] = {"carousel_index": len(env.all_image_carousels[env.docname])}

        env.all_image_carousels[env.docname].append(
            {"lineno": self.lineno, "image_carousel": node.deepcopy(), "last": True}
        )
        env.all_image_carousels[env.docname][-1]["last"] = False

        return [node]


def setup(app):
    app.add_enumerable_node(
        image_carousel,
        figtype="image-carousel",
        html=(html_visit_image_carousel, None),
    )

    app.add_directive("imagecarousel", ImageCarousel)

    app.add_css_file("image_carousel.css")
    app.add_javascript("image_carousel.js")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }