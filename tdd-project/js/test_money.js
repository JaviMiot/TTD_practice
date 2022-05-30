const assert = require('assert');

const Money = require('./money');
const Portfolio = require('./portfolio');
const Bank = require('./bank');

class MoneyTest {
    constructor() {
        this.bank = new Bank();
        this.bank.addExchangeRate("EUR", "USD", 1.2);
        this.bank.addExchangeRate("USD", "KRW", 1100);
    }

    testMultiplication() {
        let fiveEuros = new Money(5, 'EUR');
        let tenEuros = new Money(10, 'EUR');
        assert.deepStrictEqual(fiveEuros.times(2), tenEuros);
    }

    testDivision() {
        let originalMoney = new Money(4002, 'KRW');
        let actualMoneyAfterDivision = originalMoney.divide(4);
        let expectedMoneyAfterDivision = new Money(1000.5, 'KRW');
        assert.deepStrictEqual(
            actualMoneyAfterDivision,
            expectedMoneyAfterDivision
        );
    }

    testAddition() {
        let fiveDollars = new Money(5, 'USD');
        let tenDollars = new Money(10, 'USD');
        let fifteenDollars = new Money(15, 'USD');
        let portfolio = new Portfolio();
        portfolio.add(fiveDollars, tenDollars);
        assert.deepStrictEqual(portfolio.evaluate(this.bank, 'USD'), fifteenDollars);
    }

    testAdditionOfDollarsAndEuros() {
        let fiveDollars = new Money(5, 'USD');
        let tenEuros = new Money(10, 'EUR');
        let portfolio = new Portfolio();
        portfolio.add(fiveDollars, tenEuros);
        let expectedValue = new Money(17, 'USD');
        assert.deepStrictEqual(portfolio.evaluate(this.bank, 'USD'), expectedValue);
    }

    testAdditionOfDollarsAndWons() {
        let oneDollar = new Money(1, 'USD');
        let elevenHundredWons = new Money(1100, 'KRW');
        let portfolio = new Portfolio();
        portfolio.add(oneDollar, elevenHundredWons);
        let expectedValue = new Money(2200, 'KRW');
        assert.deepStrictEqual(portfolio.evaluate(this.bank, 'KRW'), expectedValue);
    }

    testAdditionWithMultipleMissingExchangeRates() {
        let oneDollar = new Money(1, 'USD');
        let oneEuro = new Money(1, 'EUR');
        let oneWon = new Money(1, 'KRW');
        let portfolio = new Portfolio();
        portfolio.add(oneDollar, oneEuro, oneWon);
        let expectedError = new Error(
            'Missing exchange rate(s):[USD->Kalganid,EUR->Kalganid,KRW->Kalganid]'
        );
        let bank = this.bank;
        assert.throws(() => portfolio.evaluate(bank, "Kalganid"), expectedError);
    }

    testConversion() {
        let tenEuros = new Money(10, 'EUR');
        assert.deepStrictEqual(this.bank.convert(tenEuros, 'USD'), new Money(12, 'USD'));
    }

    testConversionWithMissingExchangeRate() {
        let bank = this.bank;
        let tenEuros = new Money(10, "EUR");
        let expectedError = new Error("EUR->Kalganid");
        assert.throws(function () { bank.convert(tenEuros, "Kalganid"); },
            expectedError);
    }


    getAllTestMethods() {
        let moneyPrototype = MoneyTest.prototype;
        let allProps = Object.getOwnPropertyNames(moneyPrototype);
        let testMethods = allProps.filter((prop) => {
            return (
                typeof moneyPrototype[prop] === 'function' && prop.startsWith('test')
            );
        });

        return testMethods;
    }

    runAllTest() {
        const testMethods = this.getAllTestMethods();
        testMethods.forEach((method) => {
            console.log(`Running ${method}()`);
            let methodReflect = Reflect.get(this, method);

            try {
                Reflect.apply(methodReflect, this, []);
            } catch (error) {
                if (error instanceof assert.AssertionError) {
                    console.log(error);
                } else {
                    throw error;
                }
            }
        });
    }
}

new MoneyTest().runAllTest();
