// spec/calculator-spec.js

// load the testing environment
var env = require("../env.js");

// import the required files
var fn = env.path("calculator.js");
env.importJS(fn);

// perform tests
describe("multiplication", function () {
  it("should multiply 2 and 3", function () {
    var product = calculator.multiply(2, 3);
    expect(product).toBe(6);
  });
});    