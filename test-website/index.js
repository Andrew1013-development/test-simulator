const { MongoClient } = require("mongodb");

async function main() {
    // hard coded credentials again
    const username = encodeURIComponent("dontbesus");
    const password = encodeURIComponent("vb9jsbkAfXww3uc0");
    const cluster = encodeURIComponent("cluster0");

    // encode URI and create client
    let uri = `mongodb+srv://${username}:${password}@${cluster}.ygoqv7l.mongodb.net/?retryWrites=true&w=majority`;
    const client = new MongoClient(uri);

    try {
        // establish connection to database
        await client.connect();
        console.log("Established connection to the database.")
    } catch(e) {
        console.error(e);
    } finally {
        await client.close();
    }
}

main().catch(console.error);