async function runEmotionAnalysis() {
    const text = document.getElementById("textToAnalyze").value;
    const output = document.getElementById("system_response");
    output.innerHTML = "Analyzing...";

    try {
        const response = await fetch(
            `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`
        );
        output.innerHTML = await response.text();
    } catch (error) {
        output.textContent = `Unable to contact the server: ${error.message}`;
    }
}
