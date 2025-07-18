This
is
some
text
info
---
test-8
test-9
// JavaScript version
const kmsKeyId = "abcd1234-56ef-78gh-90ij-klmnopqrstuv";  // hardcoded KMS key

function encrypt(data) {
    console.log("Using KMS Key:", kmsKeyId);
    return `encrypted(${data})`;
}
