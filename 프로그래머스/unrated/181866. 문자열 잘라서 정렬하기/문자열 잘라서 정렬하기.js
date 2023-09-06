function solution(myString) {
    const words = myString.split('x').filter(word => word !== '');

    words.sort();

    return words;
}