const btn = document.getElementById('button')
const results = document.getElementById('results')
const form = document.getElementById('form')

async function getValue() {
    try {
        const req = await fetch("/filter", {
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify({
                formid: form.value
            })
        })
        const data = await req
        const text = await data.text()
            // Split text in array of strings
        const array = text.split(',')
            // Remove from array all "[ and ] and '"
        const array2 = array.map(function(item) {
                return item.replace(/[\[\]']/g, '')
            })
            // Save multiples array for each 8 elements in a new array
        const array3 = []
        for (let i = 0; i < array2.length; i += 8) {
            array3.push(array2.slice(i, i + 8))
        }
        // if array contains "404NOTFOUND" then display error message
        if (text == "404NOTFOUND") {
            results.innerHTML = `<p class="errorMsg">No se encontraron resultados de búsqueda, intenta nuevamente.</p>`
        } else {
            // Create a card for each array and append it to the results div
            array3.forEach(element => {
                const card = document.createElement('div')
                card.classList.add('dir-results-card')
                card.innerHTML = `
                    <div class="dir-results-card-header">
                        <div class="dir-card-img">
                            <img src="static/images/workers.png" alt="Colaboradores RU">
                        </div>
                        <div class="dir-card-text">
                            <p class="card-title">TERRITORIO ${element[0]}</p>
                            <p class="card-text">${element[1]}</p>
                        </div>
                    </div>
                    <div class="dir-results-card-body">
                        <div class="pdv-info">
                            <p class="card-text pdvnum">${element[2]}</p>
                            <p class="card-text pdvname">${element[3]}</p>
                        </div>
                        <div class="manager-info">
                            <p class="card-text manager"><span style="color: #000";>Gerente Líder PDV:</span> <br> ${element[4]}</p>
                            <a href="tel:${element[5]}"class="card-text managerPhone"><span>Teléfono:</span> <i class="fas fa-phone"></i> ${element[5]}</a>
                        </div>
                        <div class="leader-info">
                            <p class="card-text leader"><span style="color: #000";>Líder Comercial:</span> <br> ${element[6]}</p>
                            <a href="tel:${element[7]}" class="card-text leaderPhone"><span>Teléfono:</span> <i class="fas fa-phone"></i>${element[7]}</a>
                        </div>
                    </div>
                `
                results.appendChild(card)
            })
        }
    } catch (err) {
        console.log(err)
    }
}

btn.addEventListener('click', () => {
    results.innerHTML = ''
    if (form.value != '') {
        const request = getValue()
            // When user clicks on the button, while the request is being processed, display a loading message
        btn.innerHTML = '<i class="fas fa-sync fa-spin search-load"></i>'
        btn.disabled = true
        request.then(() => {
            btn.disabled = false
            btn.innerHTML = '<i class="search-icon fas fa-search"></i>'
        })
    }
})

form.addEventListener('keypress', (e) => {
    if (e.keyCode == 13) {
        results.innerHTML = ''
        if (form.value != '') {
            e.preventDefault()
            const request = getValue()
                // When user clicks on the button, while the request is being processed, display a loading message
            btn.innerHTML = '<i class="fas fa-sync fa-spin search-load"></i>'
            btn.disabled = true
            request.then(() => {
                btn.disabled = false
                btn.innerHTML = '<i class="search-icon fas fa-search"></i>'
            })
        }
    }
})