const Money = require('./money');

class Portfolio {
    constructor() {
        this.moneys = [];
    }
    add(...money) {
        this.moneys.push(...money);
    }

    evaluate(currency) {
        let failures = [];

        const total = this.moneys.reduce((sum, money) => {
            let convertedAmount = this.convert(money, currency);
            if (!convertedAmount) {
                failures.push(`${money.currency}->${currency}`);
                return sum;
            }
            return sum + convertedAmount;
        }, 0);

        if (!failures.length) {
            return new Money(total, currency);
        }

        throw new Error(`Missing exchange rate(s):[${failures.join(',')}]`);
    }

    convert(money, currency) {
        let exchangeRate = new Map();
        exchangeRate.set('EUR->USD', 1.2);
        exchangeRate.set('USD->KRW', 1100);

        if (money.currency === currency) {
            return money.amount;
        }

        let key = money.currency + '->' + currency;
        let rate = exchangeRate.get(key);

        if (!rate) {
            return undefined;
        }

        return money.amount * rate;
    }
}

module.exports = Portfolio;