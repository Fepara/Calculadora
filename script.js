let display = document.getElementById('display');

function appendCharacter(character) {
    display.value += character;
}

function clearDisplay() {
    display.value = '';
}

function deleteLast() {
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = 'Erro';
    }
}

function sqrt() {
    try {
        display.value = Math.sqrt(eval(display.value));
    } catch (e) {
        display.value = 'Erro';
    }
}
