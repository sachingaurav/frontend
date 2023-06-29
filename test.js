const { expect } = require("chai");

describe("Orders Page", () => {
  beforeEach(() => {
    // Load the HTML file before each test
    const jsdom = require("jsdom");
    const { JSDOM } = jsdom;
    const fs = require("fs");
    const html = fs.readFileSync("order.html", "utf-8");
    const { document } = new JSDOM(html).window;
    global.document = document;
  });

  it('should display the "Products" button', () => {
    // Assert that the "Products" button exists
    const productButton = document.querySelector(".product-button");
    expect(productButton).to.exist;

    // Assert the button text
    expect(productButton.textContent).to.contain("Products");
  });
});

after(function () {
  process.exit();
});
