const currencyE1_one = document.getElementById('currency-one');
const amountE1_one = document.getElementById('amount-one');
const currencyE1_two = document.getElementById('currency-two');
const amountE1_two = document.getElementById('amount-two');

const rateE1 = document.getElementById('rate');
const swap = document.getElementById('swap');

function caclulate() {
    const currency_one = currencyE1_one.value;
    const currency_two = currencyE1_two.value;

    fetch('https://api.exchangerate-api.com/v4/latest/${currency_one}')
        .then(res => res.json())
        .then(data => {
            const rate = data.rates[currency_two];

            rateE1.innerText = '1 ${currency_one} = ${rate} ${currency_two}';

            amountE1_two.value = (amountE1_one.value * rate).toFixed(2);
        })
}

currencyE1_one.addEventListener('change', caclulate);
amountE1_one.addEventListener('input', caclulate);
currencyE1_two.addEventListener('change', caclulate);
amountE1_two.addEventListener('input', caclulate);

swap.addEventListener('click', () => {
    const temp = currencyE1_one.value;
    currencyE1_one.value = currencyE1_two.value;
    currencyE1_two.value = temp;
    caclulate();
});

caclulate();








