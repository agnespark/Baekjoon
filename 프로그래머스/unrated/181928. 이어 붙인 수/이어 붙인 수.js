function solution(num_list) {
    var even = '';
    var odd = '';
    for (let num of num_list) {
        if (num % 2 === 0) {
            even += num.toString();
        } else {
            odd += num.toString();
        }
    }

    return parseInt(even) + parseInt(odd);
}