#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    } else {
      Object.create(null);
    }
  }

  print () {
    // print rectangle using X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width))
    }
  }
}

module.exports = Rectangle;
