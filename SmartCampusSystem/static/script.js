document.addEventListener('DOMContentLoaded', function() {
    const calculateButton = document.getElementById('calculate-gpa');
    calculateButton.addEventListener('click', function() {
      const inputText = document.getElementById('courses-input').value.trim();
      const gpaOutput = document.getElementById('gpa-output');
  
      if (!inputText) {
        gpaOutput.innerText = "Please enter your courses.";
        gpaOutput.classList.replace("text-success", "text-danger");
        return;
      }
  
      const lines = inputText.split('\n');
      let totalPoints = 0;
      let totalCredits = 0;
      let validLine = false;
  
      const gradeMap = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
        'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
      };
  
      lines.forEach(line => {
        const parts = line.trim().split(' ');
        if (parts.length >= 3) {
          const grade = parts[parts.length - 2].toUpperCase();
          const credits = parseFloat(parts[parts.length - 1]);
          if (gradeMap.hasOwnProperty(grade) && !isNaN(credits)) {
            totalPoints += gradeMap[grade] * credits;
            totalCredits += credits;
            validLine = true;
          }
        }
      });
  
      if (!validLine || totalCredits === 0) {
        gpaOutput.innerText = "Invalid format. Use: Course Grade Credits.";
        gpaOutput.classList.replace("text-success", "text-danger");
        return;
      }
  
      const gpa = (totalPoints / totalCredits).toFixed(2);
      gpaOutput.innerText = `Your GPA is: ${gpa}`;
      gpaOutput.classList.replace("text-danger", "text-success");
    });
  });
  