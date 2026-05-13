const apikey = "3d90ee10cd81bf5f4eaebf0b2cbdefb0"

const weatherDataE1 = document.getElementById('weather-data')
const cityinputE1 = document.getElementById('city-input')

const formE1 = document.querySelector('form')

formE1.addEventListener('submit', (event) => {
    event.preventDefault()

    const CityValue = cityinputE1.value

    getweatherData(CityValue)
})

async function getweatherData(CityValue) {

    try {

        const response = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${CityValue}&appid=${apikey}&units=metric`
        )

        if (!response.ok) {
            throw new Error('Network response was not ok')
        }

        const data = await response.json()

        const temperature = Math.round(data.main.temp)
        const description = data.weather[0].description
        const icon = data.weather[0].icon

        const details = [
            `Feels like: ${Math.round(data.main.feels_like)}°C`,
            `Humidity: ${data.main.humidity}%`,
            `Wind speed: ${data.wind.speed} m/s`
        ]

        weatherDataE1.querySelector('.icon').innerHTML =
            `<img src="https://openweathermap.org/img/wn/${icon}.png" alt="weather icon">`

        weatherDataE1.querySelector('.temperature').textContent =
            `${temperature}°C`

        weatherDataE1.querySelector('.description').textContent =
            description

        weatherDataE1.querySelector('.details').innerHTML =
            details.map((detail) => `<div>${detail}</div>`).join("")

    } catch (error) {

        weatherDataE1.querySelector('.icon').innerHTML = ''

        weatherDataE1.querySelector('.temperature').textContent = ''

        weatherDataE1.querySelector('.description').textContent =
            'An error happened, please try again later'

        weatherDataE1.querySelector('.details').innerHTML = ''
    }
}