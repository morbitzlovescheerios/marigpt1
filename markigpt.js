const readline = require('readline');


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const GENERIC_RESPONSES = [
    "That's a really interesting point.",
    "I'm not sure I know the answer to that, but tell me more!",
    "Hmm, I see what you mean.",
    "Could you explain that a bit more?",
    "I'm just a local script, but I'm doing my best to keep up!",
    "That sounds pretty cool.",
    "I'm listening...",
    "Wow, really?",
    "I'm learning new things every day (well, sort of).",
    "Let's keep chatting about that."
];

console.log("🔵 MarkiGPT (JavaScript Version)");
let version = "1.2";

function getResponse(input) {
    input = input.toLowerCase();
    if (input.includes("hello") || input.includes("hi")) return "Greetings! I am MarkiGPT. How can I assist you today?";
    if (input.includes("name")) return "My name is MarkiGPT 1.0 (Node.js Edition).";
    if (input.includes("joke")) return "Why did the web developer walk out of the bar? He didn't like the table layout.";
    if (input.includes("music")) return "I have deleted my music database to focus on pure intelligence.";
    if (input.includes("weather")) return "I can't see outside, but I hope it's nice wherever you are!";
    if (input.includes("meaning of life")) return "42. Obviously.";
    if (input.includes("status")) return "I'm feeling great! Systems are running smoothly.";
    if (input.includes("python") || input.includes("code")) {
        return "Here is a Python example for you:\ndef hello_world():\n    print('Hello from MarkiGPT!')";
    }
    if (input.includes("exit")) {
        console.log("Goodbye!");
        process.exit(0);
    }
    return GENERIC_RESPONSES[Math.floor(Math.random() * GENERIC_RESPONSES.length)];
}


function start() {
    rl.question('Select Version (1.2 or 1.0): ', (v) => {
        if (v.includes("1.0")) {
            version = "1.0";
            console.log("Loaded MarkiGPT 1.0 (Classic Mode). Type 'exit' to quit.\n");
        } else {
            console.log("Loaded MarkiGPT 1.2 (Modern Mode). Type 'exit' to quit.\n");
        }
        ask();
    });
}

function ask() {
    rl.question('You: ', (input) => {
        console.log('MarkiGPT: ' + getResponse(input) + '\n');
        ask();
    });
}


start();
}



ask();
