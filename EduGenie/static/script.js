async function postJSON(url, body) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  return res.json();
}

// Q&A
document.getElementById("qaForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const question = document.getElementById("question").value;
  const out = document.getElementById("qaResult");
  out.textContent = "Thinking...";
  const res = await fetch(`/qa?question=${encodeURIComponent(question)}`);
  const data = await res.json();
  out.innerHTML = `<strong>Answer:</strong>\n${data.answer || data.error}`;
});

// Explanation
document.getElementById("explainForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const topic = document.getElementById("topic").value;
  const out = document.getElementById("explanationResult");
  out.textContent = "Thinking...";
  const data = await postJSON("/explain/", { topic });
  out.innerHTML = `<strong>Explanation:</strong>\n${data.explanation || data.error}`;
});

// Summary
document.getElementById("summaryForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = document.getElementById("summaryText").value;
  const out = document.getElementById("summaryResult");
  out.textContent = "Thinking...";
  const data = await postJSON("/summarize/", { text });
  out.innerHTML = `<strong>Summary:</strong>\n${data.summary || data.error}`;
});

// Quiz
document.getElementById("quizForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = document.getElementById("quizText").value;
  const out = document.getElementById("quizResult");
  out.textContent = "Generating quiz...";
  const data = await postJSON("/quiz", { text });
  renderQuiz(out, data.quiz || []);
});

function renderQuiz(container, quiz) {
  container.innerHTML = "";
  if (!quiz.length) {
    container.textContent = "No quiz generated.";
    return;
  }
  quiz.forEach((q, i) => {
    if (q.error) {
      container.textContent = q.error;
      return;
    }
    const block = document.createElement("div");
    block.className = "quiz-question";
    const p = document.createElement("p");
    p.textContent = `Q${i + 1}: ${q.question}`;
    block.appendChild(p);

    q.options.forEach((opt) => {
      const label = document.createElement("label");
      const radio = document.createElement("input");
      radio.type = "radio";
      radio.name = `q${i}`;
      radio.value = opt;
      label.appendChild(radio);
      label.append(" " + opt);
      block.appendChild(label);
    });

    const checkBtn = document.createElement("button");
    checkBtn.textContent = "Check Answer";
    checkBtn.type = "button";
    const feedback = document.createElement("div");

    checkBtn.addEventListener("click", () => {
      const selected = block.querySelector(`input[name="q${i}"]:checked`);
      if (!selected) {
        feedback.textContent = "Please select an option.";
        return;
      }
      if (selected.value === q.answer) {
        feedback.textContent = "✅ Correct!";
        feedback.className = "correct";
      } else {
        feedback.textContent = `❌ Incorrect. Correct answer: ${q.answer}`;
        feedback.className = "incorrect";
      }
    });

    block.appendChild(checkBtn);
    block.appendChild(feedback);
    container.appendChild(block);
  });
}

// Learning Recommendations
document.getElementById("learnForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const topic = document.getElementById("learnTopic").value;
  const out = document.getElementById("learnResult");
  out.textContent = "Building your learning path...";
  const res = await fetch(`/learn/recommendations?topic=${encodeURIComponent(topic)}`);
  const data = await res.json();
  out.innerHTML = `<strong>Learning Recommendations for "${data.topic}":</strong>\n${data.recommendation}`;
});
