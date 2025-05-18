document.getElementById('start').addEventListener('click', () => {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const operation = document.getElementById('operation').value;
  const resultElement = document.getElementById('result');

  if (isNaN(num1) || isNaN(num2)) {
    resultElement.textContent = 'Please enter numbers.';
    return;
  }

  let result;

  switch (operation) {
    case 'add':
      result = num1 + num2;
      break;
    case 'sub':
      result = num1 - num2;
      break;
    case 'multi':
      result = num1 * num2;
      break;
    case 'div':
      if (num2 === 0) {
        resultElement.textContent = 'Error: Division by zero is not allowed.';
        return;
      }
      result = num1 / num2;
      break;
    default:
      resultElement.textContent = 'Unknown operation.';
      return;
  }

  resultElement.textContent = `Result: ${result}`;
});
