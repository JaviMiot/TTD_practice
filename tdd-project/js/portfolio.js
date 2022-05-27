const Money = require('./money');

class Portfolio {
    constructor() {
        this.moneys = [];
    }
    add(...money) {
        this.moneys.push(...money);
    }

    evaluate(currency) {
        const total = this.moneys.reduce((acc, money) => {
            if (money.currency === currency) {
                acc += money.amount;
            }
            return acc;
        }, 0);

        return new Money(total, currency);
    }
}

module.exports = Portfolio;