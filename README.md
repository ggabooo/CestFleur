# C’est Fleur · Galerie Florale

Proyecto completo en Python para Streamlit. Las imágenes originales están incluidas en `CATALOGO/`. No requiere Canva, una base de datos ni claves de API para funcionar.

## Publicar desde GitHub

1. Descomprime este ZIP en tu computadora.
2. Crea un repositorio en GitHub, por ejemplo `cest-fleur`.
3. En **Add file → Upload files**, sube el CONTENIDO de la carpeta `cest_fleur`: `app.py`, `catalogo.json`, `configuracion.json`, `estilos.css`, `requirements.txt`, `README.md`, y la carpeta `CATALOGO` con todas las imágenes. No subas el ZIP sin descomprimir. Conserva los nombres, mayúsculas y extensiones.
4. Incluye también `.streamlit/config.toml`. Si tu explorador no muestra esa carpeta, puedes crear el archivo en GitHub con **Add file → Create new file** y escribir `.streamlit/config.toml` como nombre. El diseño también aplica sus colores por CSS si omites ese archivo.
5. Confirma la carga con **Commit changes**.
6. Entra en https://share.streamlit.io/ y conecta tu cuenta de GitHub.
7. Selecciona **Create app**, tu repositorio y la rama donde subiste los archivos (normalmente `main`).
8. En **Main file path**, escribe `app.py`. Si subiste la carpeta completa y no su contenido, la ruta será `cest_fleur/app.py`.
9. En las opciones avanzadas usa Python 3.12, versión con la que se probó este proyecto. Pulsa **Deploy**.

## Ejecutar en tu computadora (opcional)

Con Python 3.12 instalado, abre una terminal dentro de `cest_fleur`:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Editar sin cambiar el diseño

- **Precios, nombres y descripciones:** edita `catalogo.json` directamente en GitHub y guarda con Commit changes.
- **Imágenes:** reemplaza un PNG en `CATALOGO/` conservando su nombre. Puedes agregar varios nombres en la lista `imagenes`; aparecerán en el desplegable de presentaciones.
- **Salas:** el campo `sala` admite `florale`, `mini` y `temporada`.
- **Precio por confirmar:** usa `null` (sin comillas) en `precio`. La web mostrará “Consultar precio”.
- **WhatsApp:** en `configuracion.json`, cambia `"whatsapp": ""` por tu número real con código de país, solo dígitos. Para Guatemala: 502 seguido de los 8 dígitos de tu número. Esto activa mensajes con el nombre del producto. Si queda vacío, los botones abren el perfil de Instagram del catálogo.
- **Instagram y entrega:** edita `instagram_url`, `reserva` y `envio` en `configuracion.json`.
- **Colores, tamaños y espacios:** edita `estilos.css`.

No pongas una coma después del último elemento de un objeto JSON. Conserva las comillas dobles. Cada `id` de producto debe ser único. Las imágenes se resuelven respecto a `app.py`, incluso si la aplicación está en una subcarpeta.

## Decisiones de contenido y pendientes

- Sala I: Quatre-saisons Q300; Velours Q250; Rosée Q125; Ardeur Q150; Magnifique Q175; Opulence Q250; Lumina Q150; Elixir Q150 + botella; Custom a cotizar.
- Sala II: Camaritas, Macetitas y Marquitos Q50 por unidad; Minibouquets Q30; Cerámicas Q20; Llaveros y Pines Q15. Collar incluido con precio por consultar: no se proporcionó un valor.
- Sala III: Tulipes, 10 tulipanes, Q220; disponibilidad por consultar.
- Lumina y Elixir aparecen en el PDF pero no traen imágenes individuales en el ZIP. Se incluyen como fichas de texto. Para agregar sus imágenes, sube los PNG y escribe sus nombres en `imagenes`.
- Soleil aparece en el texto extraíble del PDF, pero no en la página visible revisada ni en el ZIP; se omitió para evitar publicar una ficha residual del diseño.
- Las variantes de cada ramo se agrupan bajo su precio. En Mini se indica expresamente que el precio es por unidad, aunque la fotografía muestre varias piezas.
- Reserva con 50% de anticipo, saldo contra entrega y envío Q35 en ciudad, según el PDF. Se reformuló el texto para aclararlo.
- Los datos bancarios del PDF no se muestran en esta versión: los pedidos se coordinan por contacto.
- Las imágenes se conservan intactas en PNG; la aplicación prepara copias WebP en memoria para reducir el peso enviado al navegador.
- No se añadió carrito, pago en línea ni confirmación automática de disponibilidad. “Consultar” abre el canal de contacto; no registra ni envía un pedido por sí solo.

## Comprobación

La aplicación se ejecutó con Streamlit 1.55.0 y Python 3.12 mediante AppTest sin excepciones. Se verificaron las 18 fichas y las rutas de todas las imágenes. Se incluyeron reglas adaptables para computadora, tableta y celular. No se pudo completar una comprobación visual en navegador en el entorno de preparación; revisa la vista móvil tras publicar.

## Referencias

1. C’est Fleur. Catálogo C’est Fleur [PDF]. Documento proporcionado por el propietario; consultado 27 sep 2026.
2. C’est Fleur. Precios de C’est Fleur Mini [comunicación personal]. 27 sep 2026.
3. Streamlit. Deploy your app on Community Cloud [Internet]. [citado 27 sep 2026]. Disponible en: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
4. Streamlit. File organization for your Community Cloud app [Internet]. [citado 27 sep 2026]. Disponible en: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization
