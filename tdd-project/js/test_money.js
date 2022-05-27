const assert = require('assert');

const Money = require('./money');
const Portfolio = require('./portfolio');


class MoneyTest {

    testMultiplication() {
        let fiveEuros = new Money(5, "EUR");
        let tenEuros = new Money(10, "EUR");
        assert.deepStrictEqual(fiveEuros.times(2), tenEuros);
    }

    testDivision() {
        let originalMoney = new Money(4002, "KRW");
        let actualMoneyAfterDivision = originalMoney.divide(4);
        let expectedMoneyAfterDivision = new Money(1000.5, "KRW");
        assert.deepStrictEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision);
    }

    testAddition() {
        let fiveDollars = new Money(5, "USD");
        let tenDollars = new Money(10, "USD");
        let fifteenDollars = new Money(15, "USD");
        let portfolio = new Portfolio();
        portfolio.add(fiveDollars, tenDollars);
        assert.deepStrictEqual(portfolio.evaluate('USD'), fifteenDollars);
    }

    getAllTestMethods() {
        let moneyPrototype = MoneyTest.prototype;
        let allProps = Object.getOwnPropertyNames(moneyPrototype);
        let testMethods = allProps.filter(prop => {
            return typeof moneyPrototype[prop] === 'function' && prop.startsWith('test');
        });

        return testMethods;
    }

    runAllTest() {
        const testMethods = this.getAllTestMethods();
        testMethods.forEach(method => {
            let methodReflect = Reflect.get(this, method);
            Reflect.apply(methodReflect, this, []);
        });
    }

}

new MoneyTest().runAllTest();