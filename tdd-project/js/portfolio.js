const Money = require('./money');

class Portfolio {
    constructor() {
        this.moneys = [];
    }
    add(...money) {
        this.moneys.push(...money);
    }

    evaluate(bank, currency) {
        let failures = [];

        const total = this.moneys.reduce((sum, money) => {
            try {
                let convertedMoney = bank.convert(money, currency);
                return sum + convertedMoney.amount;
            } catch (error) {
                failures.push(error.message);
                return sum;
            }
        }, 0);

        if (!failures.length) {
            return new Money(total, currency);
        }

        throw new Error(`Missing exchange rate(s):[${failures.join(',')}]`);
    }

}

module.exports = Portfolio;