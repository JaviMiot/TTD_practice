const Money = require('./money');

class Bank {

    constructor() {
        this.exchangeRates = new Map();
    }
    addExchangeRate(from, to, rate) {
        this.exchangeRates.set(`${from}->${to}`, rate);
    }

    convert(money, to) {
        if (money.currency === to) {
            return new Money(money.amount, money.currency);
        }

        let key = `${money.currency}->${to}`;
        let rate = this.exchangeRates.get(key);

        if (rate === undefined) {
            throw new Error(key);
        }
        return new Money(money.amount * rate, to);
    }
}

module.exports = Bank;