// __author__ = vkremez

image = new SimpleImage("___.jpg");
back = new SimpleImage("____.jpg");
back.setSameSize(image);

for (pixel: image) {
  avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue())/3;
  if (pixel.getBlue() > avg * 1.1) {
    x = pixel.getX();
    y = pixel.getY();
    pixel2 = back.getPixel(x, y);
    pixel.setRed(pixel2.getRed());
    pixel.setGreen(pixel2.getGreen());
    pixel.setBlue(pixel2.getBlue());
}
}
print(image);
