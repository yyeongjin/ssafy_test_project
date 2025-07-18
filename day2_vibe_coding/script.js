// 대화 내역을 저장하는 배열 (system 프롬프트 포함)
let messages = [
    { role: 'system', content: 'You are a helpful assistant.' }
];

// 오늘의 주식 리스트 (예시)
const stocks = [
    { name: '삼성전자', price: 80000, change: 2.1 },
    { name: 'SK하이닉스', price: 190000, change: -1.5 },
    { name: '네이버', price: 210000, change: 0.7 },
    { name: '카카오', price: 54000, change: -2.3 },
    { name: 'LG에너지솔루션', price: 410000, change: 3.2 },
    { name: '현대차', price: 220000, change: -0.8 },
    { name: 'POSCO홀딩스', price: 500000, change: 1.9 },
    { name: '셀트리온', price: 170000, change: -3.0 }
];

function showWelcomeStock() {
    const chatBox = document.getElementById('chat-box');
    const stock = stocks[Math.floor(Math.random() * stocks.length)];
    const upDown = stock.change >= 0 ? '▲' : '▼';
    const msg = `오늘의 주식: ${stock.name} (${stock.price.toLocaleString()}원) ${upDown} ${stock.change}%`;
    const botMsg = document.createElement('div');
    botMsg.className = 'message bot';
    botMsg.textContent = msg;
    chatBox.appendChild(botMsg);
    // 표정: 상승이면 기쁨, 하락이면 화남
    if (stock.change >= 0) {
        document.getElementById('ai-face').textContent = '😄';
        document.getElementById('ai-temp').style.width = '90%';
    } else {
        document.getElementById('ai-face').textContent = '😡';
        document.getElementById('ai-temp').style.width = '10%';
    }
    chatBox.scrollTop = chatBox.scrollHeight;
    // 대화 내역에도 추가
    messages.push({ role: 'assistant', content: msg });
}

// 실시간 AI 온도 그래프 데이터 관리
let aiTempHistory = [];
const MAX_TEMP_HISTORY = 50;
function updateAITempGraph(temp) {
    aiTempHistory.push(temp);
    if (aiTempHistory.length > MAX_TEMP_HISTORY) aiTempHistory.shift();
    const graph = document.getElementById('ai-temp-graph');
    if (!graph) return;
    graph.innerHTML = '';
    // 라벨 영역 생성
    const labelDiv = document.createElement('div');
    labelDiv.id = 'ai-temp-graph-label';
    labelDiv.style.fontSize = '22px';
    labelDiv.style.fontWeight = 'bold';
    labelDiv.style.marginBottom = '18px';
    labelDiv.style.textAlign = 'center';
    labelDiv.style.letterSpacing = '2px';
    labelDiv.style.color = '#1976d2';
    labelDiv.style.textShadow = '0 2px 8px #90caf9';
    labelDiv.textContent = '실시간 AI 온도';
    graph.appendChild(labelDiv);
    // 1:2:1 비율에 맞춰 SVG 크기 동적 계산
    const w = graph.offsetWidth || 360;
    const h = (graph.offsetHeight || 720) - labelDiv.offsetHeight - 18;
    const pad = Math.max(24, Math.floor(w * 0.07));
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('width', w);
    svg.setAttribute('height', h);
    svg.style.background = 'linear-gradient(135deg, #f5fafd 0%, #e3f2fd 100%)';
    svg.style.borderRadius = '16px';
    svg.style.display = 'block';
    svg.style.margin = '0 auto';
    svg.style.boxShadow = '0 2px 16px #90caf988';
    // 꺾은선
    let points = aiTempHistory.map((t, i) => {
        const x = pad + (w - 2 * pad) * (i / (MAX_TEMP_HISTORY - 1));
        const y = h - pad - (t / 100) * (h - 2 * pad);
        return `${x},${y}`;
    }).join(' ');
    if (aiTempHistory.length > 1) {
        const polyline = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
        polyline.setAttribute('points', points);
        polyline.setAttribute('fill', 'none');
        polyline.setAttribute('stroke', '#1976d2');
        polyline.setAttribute('stroke-width', Math.max(3, Math.floor(w * 0.012)));
        polyline.setAttribute('filter', 'url(#shadow)');
        svg.appendChild(polyline);
    }
    // 점 표시
    aiTempHistory.forEach((t, i) => {
        const x = pad + (w - 2 * pad) * (i / (MAX_TEMP_HISTORY - 1));
        const y = h - pad - (t / 100) * (h - 2 * pad);
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', x);
        circle.setAttribute('cy', y);
        circle.setAttribute('r', Math.max(5, Math.floor(w * 0.018)));
        circle.setAttribute('fill', '#ffb74d');
        circle.setAttribute('stroke', '#1976d2');
        circle.setAttribute('stroke-width', '2');
        svg.appendChild(circle);
    });
    // y축 눈금 표시
    for (let i = 0; i <= 100; i += 25) {
        const y = h - pad - (i / 100) * (h - 2 * pad);
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', pad);
        line.setAttribute('x2', w - pad);
        line.setAttribute('y1', y);
        line.setAttribute('y2', y);
        line.setAttribute('stroke', '#b3e5fc');
        line.setAttribute('stroke-dasharray', '6 6');
        svg.appendChild(line);
        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        label.setAttribute('x', 8);
        label.setAttribute('y', y + 8);
        label.setAttribute('font-size', Math.max(14, Math.floor(w * 0.035)) + 'px');
        label.setAttribute('fill', '#1976d2');
        label.setAttribute('font-weight', 'bold');
        label.textContent = i;
        svg.appendChild(label);
    }
    // 그림자 효과
    const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    defs.innerHTML = `<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#90caf9"/></filter>`;
    svg.appendChild(defs);
    graph.appendChild(svg);
}

function setAIFaceAndTemp(text) {
    let angryWords = ['짜증', '화나', '빡쳐', '싫어', '불만', '최악', '실망', '화났', '분노', '짜증나', '열받', '불쾌', '짜증이', '화가', '화났어'];
    let happyWords = ['좋아', '기뻐', '행복', '최고', '감사', '고마워', '멋져', '즐거워', '신나', '기쁘다', '행복해', '만족', '기쁨'];
    let sadWords = ['슬퍼', '아쉬워', '속상', '눈물', '힘들', '외로워', '우울', '실망', '슬픔', '울고', '울었', '서운', '아프다'];
    const lower = text.toLowerCase();
    let face = '😊';
    let temp = 50;
    if (angryWords.some(w => lower.includes(w))) {
        face = '😡'; temp = Math.max(5, Math.floor(Math.random() * 15)); // 5~15
    } else if (happyWords.some(w => lower.includes(w))) {
        face = '😄'; temp = Math.min(95, 85 + Math.floor(Math.random() * 15)); // 85~99
    } else if (sadWords.some(w => lower.includes(w))) {
        face = '😢'; temp = Math.max(20, Math.floor(Math.random() * 20) + 20); // 20~39
    } else {
        face = '😊'; temp = 50 + Math.floor(Math.random() * 10) - 5; // 45~55
    }
    document.getElementById('ai-face').textContent = face;
    document.getElementById('ai-temp').style.width = temp + '%';
    updateAITempGraph(temp);
}

function formatTime(date) {
    return date.toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' });
}

function saveChatHistory() {
    localStorage.setItem('chatHistory', JSON.stringify(messages));
}

function loadChatHistory() {
    const chatBox = document.getElementById('chat-box');
    const history = localStorage.getItem('chatHistory');
    if (history) {
        const loaded = JSON.parse(history);
        // 기존 메시지 배열 초기화 후 불러오기
        messages = loaded;
        chatBox.innerHTML = '';
        loaded.forEach(msg => {
            if (msg.role === 'user' || msg.role === 'assistant') {
                const div = document.createElement('div');
                div.className = 'message ' + (msg.role === 'user' ? 'user' : 'bot');
                div.textContent = msg.content;
                // 시간 표시 (저장된 시간 있으면, 없으면 현재)
                const timeSpan = document.createElement('span');
                timeSpan.className = 'msg-time';
                timeSpan.textContent = msg.time ? msg.time : '';
                timeSpan.style.float = 'right';
                timeSpan.style.fontSize = '12px';
                timeSpan.style.color = '#888';
                timeSpan.style.marginLeft = '8px';
                div.appendChild(timeSpan);
                chatBox.appendChild(div);
            }
        });
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

// 여러 채팅 세션 저장 기능
function getAllChats() {
    const all = localStorage.getItem('allChats');
    return all ? JSON.parse(all) : [];
}
function saveCurrentChat() {
    // 현재 messages를 새로운 세션으로 저장
    let all = getAllChats();
    // 시간, 첫 메시지, id 등으로 구분
    const chatId = Date.now();
    all.push({
        id: chatId,
        title: messages.find(m => m.role === 'user')?.content?.slice(0, 20) || '새 채팅',
        time: new Date().toISOString(),
        messages: messages
    });
    localStorage.setItem('allChats', JSON.stringify(all));
}
function showChatList() {
    let all = getAllChats();
    let listDiv = document.getElementById('chat-list');
    if (!listDiv) {
        listDiv = document.createElement('div');
        listDiv.id = 'chat-list';
        listDiv.style.marginTop = '16px';
        listDiv.style.padding = '8px';
        listDiv.style.background = '#f7fcff';
        listDiv.style.borderRadius = '8px';
        listDiv.style.boxShadow = '0 2px 8px #b2eaff22';
        document.querySelector('.chat-container').insertBefore(listDiv, document.querySelector('#chat-box'));
    }
    listDiv.innerHTML = '<b>저장된 채팅 목록</b><br>';
    all.forEach(chat => {
        const btn = document.createElement('button');
        btn.textContent = chat.title + ' (' + new Date(chat.time).toLocaleString('ko-KR') + ')';
        btn.className = 'chat-list-btn';
        btn.style.margin = '4px 0';
        btn.style.width = '100%';
        btn.style.borderRadius = '6px';
        btn.style.border = '1px solid #b2eaff';
        btn.style.background = '#e0f7fa';
        btn.style.color = '#222';
        btn.style.fontSize = '14px';
        btn.style.cursor = 'pointer';
        btn.onclick = function() {
            messages = chat.messages;
            localStorage.setItem('chatHistory', JSON.stringify(messages));
            loadChatHistory();
        };
        listDiv.appendChild(btn);
    });
}

// 새채팅 버튼 클릭 시 현재 대화 저장 후 초기화
function clearChatHistory() {
    saveCurrentChat();
    localStorage.removeItem('chatHistory');
    messages = [
        { role: 'system', content: 'You are a helpful assistant.' }
    ];
    document.getElementById('chat-box').innerHTML = '';
    showWelcomeStock();
    showChatList();
}

// ChatGPT 스타일 사이드바 UI 생성 및 동작
function renderSidebar() {
    let sidebar = document.getElementById('sidebar');
    if (!sidebar) {
        sidebar = document.createElement('div');
        sidebar.id = 'sidebar';
        document.body.appendChild(sidebar);
    }
    sidebar.innerHTML = '';
    const title = document.createElement('h3');
    title.textContent = '채팅 목록';
    sidebar.appendChild(title);
    // 새채팅 버튼
    const newChatBtn = document.createElement('button');
    newChatBtn.id = 'new-chat-sidebar-btn';
    newChatBtn.textContent = '새 채팅';
    newChatBtn.onclick = function() {
        clearChatHistory();
        sidebar.classList.remove('open');
    };
    sidebar.appendChild(newChatBtn);
    // 채팅 목록
    const all = getAllChats();
    all.slice().reverse().forEach(chat => {
        const btn = document.createElement('button');
        btn.textContent = chat.title + ' (' + new Date(chat.time).toLocaleString('ko-KR') + ')';
        btn.className = 'chat-list-btn';
        btn.onclick = function() {
            messages = chat.messages;
            localStorage.setItem('chatHistory', JSON.stringify(messages));
            loadChatHistory();
            sidebar.classList.remove('open');
        };
        sidebar.appendChild(btn);
    });
}
function setupSidebarToggle() {
    let toggleBtn = document.getElementById('sidebar-toggle');
    if (!toggleBtn) {
        toggleBtn = document.createElement('button');
        toggleBtn.id = 'sidebar-toggle';
        toggleBtn.innerHTML = '&#9776;'; // 햄버거 아이콘
        document.body.appendChild(toggleBtn);
    }
    toggleBtn.onclick = function() {
        const sidebar = document.getElementById('sidebar');
        if (sidebar) {
            sidebar.classList.toggle('open');
        }
    };
}
window.addEventListener('DOMContentLoaded', function() {
    showWelcomeStock();
    let graph = document.getElementById('ai-temp-graph');
    if (!graph) {
        graph = document.createElement('div');
        graph.id = 'ai-temp-graph';
        graph.style.position = 'fixed';
        graph.style.top = '32px';
        graph.style.right = '32px';
        graph.style.width = '360px';
        graph.style.height = '720px';
        graph.style.maxWidth = '400px';
        graph.style.maxHeight = '800px';
        graph.style.minWidth = '200px';
        graph.style.minHeight = '400px';
        graph.style.zIndex = '100';
        graph.style.background = 'linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%)'; // 산뜻한 블루톤 그라데이션
        graph.style.borderRadius = '24px';
        graph.style.boxShadow = '0 8px 32px #b2eaff55';
        graph.style.border = '2px solid #90caf9';
        graph.style.pointerEvents = 'none';
        document.body.appendChild(graph);
    }
    const toggle = document.getElementById('mode-toggle');
    if (toggle) {
        toggle.addEventListener('change', function() {
            document.body.classList.toggle('dark', toggle.checked);
        });
    }
    const input = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    if (input) {
        input.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                sendMessage();
            }
        });
    }
    if (sendBtn) {
        sendBtn.addEventListener('click', function() {
            sendMessage();
        });
    }
    renderSidebar();
    setupSidebarToggle();
    loadChatHistory();
    showChatList();

    // 로고 추가 (상단 중앙)
    let logo = document.getElementById('custom-logo');
    if (!logo) {
        logo = document.createElement('div');
        logo.id = 'custom-logo';
        logo.style.position = 'fixed';
        logo.style.top = '16px';
        logo.style.left = '50%';
        logo.style.transform = 'translateX(-50%)';
        logo.style.zIndex = '200';
        logo.style.display = 'flex';
        logo.style.alignItems = 'center';
        logo.style.justifyContent = 'center';
        logo.style.gap = '12px';
        logo.style.background = 'linear-gradient(90deg, #90caf9 0%, #1976d2 100%)';
        logo.style.borderRadius = '32px';
        logo.style.boxShadow = '0 4px 16px #b2eaff55';
        logo.style.padding = '10px 32px';
        logo.style.fontFamily = 'Segoe UI, Arial, sans-serif';
        logo.style.fontWeight = 'bold';
        logo.style.fontSize = '28px';
        logo.style.color = '#fff';
        logo.style.letterSpacing = '2px';
        logo.innerHTML = `
            <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="20" cy="20" r="18" fill="#fff" stroke="#1976d2" stroke-width="3"/>
                <path d="M12 24 Q20 32 28 24" stroke="#1976d2" stroke-width="2.5" fill="none"/>
                <ellipse cx="15" cy="17" rx="2.5" ry="3.5" fill="#90caf9"/>
                <ellipse cx="25" cy="17" rx="2.5" ry="3.5" fill="#90caf9"/>
                <circle cx="15" cy="17" r="1.2" fill="#1976d2"/>
                <circle cx="25" cy="17" r="1.2" fill="#1976d2"/>
            </svg>
            <span>AI Chat Summer</span>
        `;
        document.body.appendChild(logo);
    }
});

async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const apiKey = document.getElementById('api-key').value.trim();
    const userText = input.value.trim();
    if (userText === '') return;

    // 사용자 메시지 추가 (텔레그램 스타일)
    const userMsg = document.createElement('div');
    userMsg.className = 'message user';
    userMsg.style.background = '#e3f2fd';
    userMsg.style.borderRadius = '12px';
    userMsg.style.padding = '10px 16px';
    userMsg.style.margin = '8px 0';
    userMsg.style.maxWidth = '70%';
    userMsg.style.boxShadow = '0 2px 8px #b2eaff22';
    userMsg.style.display = 'inline-block';
    userMsg.style.wordBreak = 'break-word';
    userMsg.textContent = userText;
    // 답변 시간 표시
    const userTime = document.createElement('span');
    userTime.className = 'msg-time';
    userTime.textContent = formatTime(new Date());
    userTime.style.float = 'right';
    userTime.style.fontSize = '12px';
    userTime.style.color = '#888';
    userTime.style.marginLeft = '8px';
    userMsg.appendChild(userTime);
    chatBox.appendChild(userMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = '';

    // 대화 내역에 사용자 메시지 추가
    messages.push({ role: 'user', content: userText, time: formatTime(new Date()) });
    saveChatHistory();

    // API 키 없으면 안내
    if (!apiKey) {
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.style.background = '#fffde7';
        botMsg.style.borderRadius = '12px';
        botMsg.style.padding = '10px 16px';
        botMsg.style.margin = '8px 0';
        botMsg.style.maxWidth = '70%';
        botMsg.style.boxShadow = '0 2px 8px #ffe08244';
        botMsg.style.display = 'inline-block';
        botMsg.style.wordBreak = 'break-word';
        botMsg.textContent = 'OpenAI API 키를 입력해주세요.';
        const botTime = document.createElement('span');
        botTime.className = 'msg-time';
        botTime.textContent = formatTime(new Date());
        botTime.style.float = 'right';
        botTime.style.fontSize = '12px';
        botTime.style.color = '#888';
        botTime.style.marginLeft = '8px';
        botMsg.appendChild(botTime);
        chatBox.appendChild(botMsg);
        setAIFaceAndTemp('');
        chatBox.scrollTop = chatBox.scrollHeight;
        return;
    }

    // 그림 요청이면 아스키아트로 안내
    if (/그림|draw|image|사진|picture|그려|그려줘|그려볼래|그려봐|그려줄래/i.test(userText)) {
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.style.background = '#fffde7';
        botMsg.style.borderRadius = '12px';
        botMsg.style.padding = '10px 16px';
        botMsg.style.margin = '8px 0';
        botMsg.style.maxWidth = '70%';
        botMsg.style.boxShadow = '0 2px 8px #ffe08244';
        botMsg.style.display = 'inline-block';
        botMsg.style.wordBreak = 'break-word';
        botMsg.textContent = 'AI는 그림 요청에 대해 아스키아트로만 응답합니다.';
        const botTime = document.createElement('span');
        botTime.className = 'msg-time';
        botTime.textContent = formatTime(new Date());
        botTime.style.float = 'right';
        botTime.style.fontSize = '12px';
        botTime.style.color = '#888';
        botTime.style.marginLeft = '8px';
        botMsg.appendChild(botTime);
        chatBox.appendChild(botMsg);
        setAIFaceAndTemp('');
        chatBox.scrollTop = chatBox.scrollHeight;
        messages.push({ role: 'assistant', content: 'AI는 그림 요청에 대해 아스키아트로만 응답합니다.', time: formatTime(new Date()) });
        saveChatHistory();
        return;
    }

    // OpenAI API 호출
    const url = 'https://api.openai.com/v1/chat/completions';
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey
    };
    // 그림 요청 여부 판별
    const isImageRequest = /그림|draw|image|사진|picture|그려|그려줘|그려볼래|그려봐|그려줄래/i.test(userText);
    let systemPrompt = 'You are a helpful assistant.';
    if (isImageRequest) {
        systemPrompt += ' If the user requests any image, drawing, or picture, always respond with ASCII art only.';
    }
    const body = JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [
            { role: 'system', content: systemPrompt },
            ...messages.filter(m => m.role !== 'system')
        ]
    });
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: body
        });
        if (!response.ok) throw new Error('API 오류: ' + response.status);
        const data = await response.json();
        const botText = data.choices?.[0]?.message?.content || '응답을 받을 수 없습니다.';
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.style.background = '#fffde7';
        botMsg.style.borderRadius = '12px';
        botMsg.style.padding = '10px 16px';
        botMsg.style.margin = '8px 0';
        botMsg.style.maxWidth = '70%';
        botMsg.style.boxShadow = '0 2px 8px #ffe08244';
        botMsg.style.display = 'inline-block';
        botMsg.style.wordBreak = 'break-word';
        // 그림 요청이면 아스키아트는 pre 태그로 표시
        if (isImageRequest || /```|\n|\s{2,}/.test(botText)) {
            const pre = document.createElement('pre');
            pre.textContent = botText;
            pre.style.background = '#fffde7';
            pre.style.borderRadius = '8px';
            pre.style.padding = '8px';
            pre.style.margin = '4px 0';
            pre.style.fontFamily = 'monospace';
            pre.style.fontSize = '14px';
            botMsg.appendChild(pre);
        } else {
            botMsg.textContent = botText;
        }
        // 답변 시간 표시
        const botTime = document.createElement('span');
        botTime.className = 'msg-time';
        botTime.textContent = formatTime(new Date());
        botTime.style.float = 'right';
        botTime.style.fontSize = '12px';
        botTime.style.color = '#888';
        botTime.style.marginLeft = '8px';
        botMsg.appendChild(botTime);
        chatBox.appendChild(botMsg);
        setAIFaceAndTemp(botText);
        chatBox.scrollTop = chatBox.scrollHeight;
        // 대화 내역에 챗봇 답변 추가
        messages.push({ role: 'assistant', content: botText, time: formatTime(new Date()) });
        saveChatHistory();
    } catch (err) {
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.style.background = '#fffde7';
        botMsg.style.borderRadius = '12px';
        botMsg.style.padding = '10px 16px';
        botMsg.style.margin = '8px 0';
        botMsg.style.maxWidth = '70%';
        botMsg.style.boxShadow = '0 2px 8px #ffe08244';
        botMsg.style.display = 'inline-block';
        botMsg.style.wordBreak = 'break-word';
        botMsg.textContent = 'API 호출 오류: ' + err.message;
        const botTime = document.createElement('span');
        botTime.className = 'msg-time';
        botTime.textContent = formatTime(new Date());
        botTime.style.float = 'right';
        botTime.style.fontSize = '12px';
        botTime.style.color = '#888';
        botTime.style.marginLeft = '8px';
        botMsg.appendChild(botTime);
        chatBox.appendChild(botMsg);
        setAIFaceAndTemp('');
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
