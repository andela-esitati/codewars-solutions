function remove(s) {
    //coding and coding....
    words = s.split("");
    let lastWord = words.pop();
    if (lastWord === "!") {
        let finalWords = words.join("");
        return finalWords;
    } else {
        words.push(lastWord);
        let finalWords = words.join("");
        return finalWords;
    }
}