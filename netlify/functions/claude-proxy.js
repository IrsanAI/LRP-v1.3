exports.handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
      },
      body: '',
    };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  try {
    const incoming = JSON.parse(event.body);

    // Convert Anthropic format → Groq (OpenAI-compatible)
    const groqBody = {
      model: 'llama-3.3-70b-versatile',
      max_tokens: incoming.max_tokens || 1000,
      temperature: 0.7,
      messages: [
        ...(incoming.system ? [{ role: 'system', content: incoming.system }] : []),
        ...incoming.messages,
      ],
    };

    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.GROQ_API_KEY}`,
      },
      body: JSON.stringify(groqBody),
    });

    const data = await response.json();

    // Convert Groq response → Anthropic format (so HTML needs no change)
    const translated = {
      content: [{
        type: 'text',
        text: data.choices?.[0]?.message?.content || '',
      }]
    };

    return {
      statusCode: response.ok ? 200 : response.status,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify(translated),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};
