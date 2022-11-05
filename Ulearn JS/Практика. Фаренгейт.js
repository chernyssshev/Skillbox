function convertCelsiusToFahrenheit (degrees) {
    const tempCelsius = degrees
    const CelsiusToFahrenheit = tempCelsius * 9 / 5 + 32
        console.log(CelsiusToFahrenheit)
}
currentDegrees = prompt ('Введите число градусов: ')
convertCelsiusToFahrenheit(currentDegrees)
