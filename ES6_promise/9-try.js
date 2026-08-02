export default function guardrail(mathFunction) {
    const queue = [];
  
    try {
      const result = mathFunction();
      queue.push(result);
    } catch (error) {
      // Converts the error object to its string representation ("Error: message")
      queue.push(error.toString());
    } finally {
      queue.push('Guardrail was processed');
    }
  
    return queue;
  }