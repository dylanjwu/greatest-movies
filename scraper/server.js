const express = require('express');
const cors = require('cors');
const fs = require('fs');
require('nodemon');

const app = express();
app.use(cors());
app.use(express.urlencoded({ extended: false }));
const port = 3000

const LIST_FILE = '/movie_data.json';

function openFile(path) {
    const data = fs.readFileSync(process.cwd() + path);
    return JSON.parse(data);
}

const fileContents = openFile(LIST_FILE);

app.get('/', (req, res) => {
    res.send(fileContents);
})

app.listen(port, () => { console.log(`Example app listening at http://localhost:${port}`) });