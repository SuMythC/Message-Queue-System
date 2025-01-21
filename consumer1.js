export async function handler(event) { 
    console.log(JSON.stringify(event));
    const o = JSON.parse(event.Records[0].body); 
    console.log('Received: ', o);
    console.log('Consumer #1 Consuming...'); 
    await sleep(5000);
}

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}
