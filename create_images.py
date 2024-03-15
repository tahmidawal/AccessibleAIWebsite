import xml.etree.ElementTree as ET
from PIL import Image


def remove_background_make_black_white(image_path, output_path):
    # Load the image
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        # If the pixel is black, change it to white. Otherwise, make it transparent.
        if item[0] == 0 and item[1] == 0 and item[2] == 0:  # black
            newData.append((255, 255, 255, 255))  # changing black to white
        else:
            # making everything else transparent
            newData.append((255, 255, 255, 0))

    # Update image data
    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Image saved to {output_path}")


def modify_svg_colors(svg_path, output_path):
    # Namespace may be required to parse SVG files properly
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', namespaces['svg'])

    # Load the SVG file
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Iterate over all elements in the SVG
    for elem in root.iterfind('.//svg:*', namespaces):
        # Check if this element has a 'fill' attribute
        fill = elem.get('fill')
        if fill:
            # Change black fills to white
            if fill.lower() in ['#000', '#000000', 'black']:
                elem.set('fill', '#ffffff')
            else:
                # Make everything else transparent
                elem.set('fill', 'none')

        # Similar approach can be applied to 'stroke' or other attributes
        stroke = elem.get('stroke')
        if stroke:
            if stroke.lower() in ['#000', '#000000', 'black']:
                elem.set('stroke', '#ffffff')
            else:
                elem.set('stroke', 'none')

    # Save the modified SVG
    tree.write(output_path)
    print(f"Modified SVG saved to {output_path}")

# Example usage


# Example usage
remove_background_make_black_white("/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/data-analysis-no-bg.png",
                                   "/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/data-analysis-no-bg-white.png")
remove_background_make_black_white("/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/data-extraction-no-bg.png",
                                   "/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/data-extraction-no-bg-white.png")
remove_background_make_black_white("/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/essay-writing-no-bg.png",
                                   "/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/essay-writing-no-bg-white.png")
remove_background_make_black_white("/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/excel-automation-no-bg.png",
                                   "/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/excel-automation-no-bg-white.png")
remove_background_make_black_white("/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/web-scraping-no-bg.png",
                                   "/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/web-scraping-no-bg-white.png")
remove_background_make_black_white("/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/infinite-icon.png",
                                   "/Users/camabernethy/Documents/Vesperr/assets/img/custom-ai-systems/infinite-icon-no-bg-white.png")
