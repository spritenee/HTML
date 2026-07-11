document.addEventListener("DOMContentLoaded", async function() {
  const tag = ['p', 'r', 'e'].join('');
  const codeBlocks = document.querySelectorAll(tag);
  let hasMermaid = false;
  
  for (const block of codeBlocks) {
    const text = block.textContent;
    
    // 💡 核心防御机制：如果内容包含 graph TD，但同时包含了 JS 的特征词，说明它是你在文章里分享的代码，绝对不要渲染！
    if (text.includes('document.addEventListener') || text.includes('const codeBlocks') || text.includes('querySelectorAll')) {
      continue; // 触发免死金牌，直接跳过，保留它作为干净的代码块显示
    }

    if (text.includes('graph TD') || block.className.includes('plaintext') || block.className.includes('mermaid')) {
      try {
        hasMermaid = true;
        
        let rawCode = text;
        if (!rawCode.includes('\n') || rawCode.match(/\n/g).length < 3) {
          rawCode = rawCode
            .replace(/graph TD\s*/g, 'graph TD\n')
            .replace(/\s*([A-G](?=\[|\{))/g, '\n$1')
            .replace(/\s*([A-G]\s*-->)/g, '\n$1')
            .replace(/\s*(style\s+[A-G])/g, '\n$1');
        }

        const container = document.createElement('div');
        container.className = 'mermaid';
        container.style.width = '100%';
        container.style.margin = '24px 0';
        container.style.background = 'transparent';
        container.style.display = 'flex';
        container.style.justifyContent = 'center';
        container.textContent = rawCode;
        
        let targetElement = block;
        const figureShell = block.closest('figure.highlight');
        if (figureShell) {
          targetElement = figureShell;
        } else if (block.parentNode && block.parentNode.tagName === 'DIV') {
          targetElement = block.parentNode;
        }
        
        targetElement.parentNode.insertBefore(container, targetElement);
        targetElement.remove();
        
      } catch(e) {
        console.error('De-shelling failed:', e);
      }
    }
  }

  if (hasMermaid) {
    const { default: mermaid } = await import('https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs');
    mermaid.initialize({ 
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose',
      flowchart: { useMaxWidth: false, htmlLabels: true }
    });
    await mermaid.run();
  }
});