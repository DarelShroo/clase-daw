const containerInfoNavegador = document.querySelector(
  '.container-info-navegador'
);

const { userAgent, language, platform, userAgentData } = navigator;

let name = 'Desconocido';
let version = 'Desconocida';

if (userAgentData) {
  const brand = userAgentData.brands?.[0];
  if (brand) {
    name = brand.brand;
    version = brand.version;
  }
} else {
  const match = userAgent.match(
    /(firefox|msie|chrome|safari|edg|opr|opera)[\/\s]?([\d.]+)/i
    /*
    /                     → Delimitador de inicio del regex
    (firefox|msie|chrome|safari|edg|opr|opera)
                          → Grupo de captura 1: detecta uno de los navegadores listados
    [\/\s]?               → Opcional: puede aparecer '/' o un espacio entre el nombre y la versión
    ([\d.]+)              → Grupo de captura 2: coincide con la versión del navegador (dígitos y puntos)
    /i                    → Modificador 'i': hace que el regex no distinga mayúsculas de minúsculas
  */
  );
  if (match) {
    name = match[1];
    version = match[2];
  }
}

const containerAllData = document.getElementById('container-all-data');

containerAllData.innerHTML = `
        <p><strong>Nombre del navegador:</strong> <span id="browser-name">${name}</span></p>
        <p><strong>Versión del navegador:</strong><span id="browser-version">${version}</span></p>
        <p><strong>Plataforma:</strong> <span id="platform">${platform}</span></p>
        <p><strong>Lenguaje:</strong> <span id="language">${language}</span></p>
        <p><strong>User Agent:</strong> <span id="user-agent">${userAgent}</span></p>
        <p><strong>Resolución de pantalla:</strong> ${screen.width} x ${screen.height}</p>
        <p><strong>Tamaño de ventana:</strong> ${window.innerWidth} x ${window.innerHeight}</p>
        <p><strong>Cookies habilitadas:</strong> ${navigator.cookieEnabled}</p>
        <p><strong>Estado conexión:</strong> ${navigator.onLine ? 'Online' : 'Offline'}</p>`;
