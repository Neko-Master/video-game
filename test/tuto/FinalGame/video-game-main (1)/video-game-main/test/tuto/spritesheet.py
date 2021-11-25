#Code from taken and slightliy adapted:
#https://stackoverflow.com/questions/45526988/does-anyone-have-an-example-of-using-sprite-sheets-in-tandem-with-xml-files
import xml.etree.ElementTree as ET
import pygame


class SpriteSheet:
    # load an atlas image
    # can also pass an associated XML file (ref. Kenney art)
    def __init__(self, img_file, data_file=None):
        self.spritesheet = pygame.image.load(img_file).convert_alpha()
        if data_file:
            tree = ET.parse(data_file)
            self.map = {}
            for node in tree.iter():
                if node.attrib.get('name'):
                    name = node.attrib.get('name')
                    self.map[name] = {}
                    self.map[name]['x'] = int(node.attrib.get('x'))
                    self.map[name]['y'] = int(node.attrib.get('y'))
                    self.map[name]['width'] = int(node.attrib.get('width'))
                    self.map[name]['height'] = int(node.attrib.get('height'))

    def get_image_rect(self, x, y, w, h):
        return self.spritesheet.subsurface(pygame.Rect(x, y, w, h))
    #default tile size is 50*50 but can changed how you like
    def get_image_name(self, name, width=50,height=50):
        rect = pygame.Rect(self.map[name]['x'], self.map[name]['y'],
                       self.map[name]['width'], self.map[name]['height'])
        return pygame.transform.scale(self.spritesheet.subsurface(rect),(width,height))