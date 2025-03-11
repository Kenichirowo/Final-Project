import streamlit as st

st.title("Movie releases per Genre")

# Embed the Tableau visualization using an iframe and JavaScript
tableau_embed_code = """
<div class='tableauPlaceholder' id='viz1741455365311' style='position: relative'><noscript><a href='#'><img alt='Historical Genre production ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ED&#47;EDA_17414513643700&#47;HistoricalGenreproduction&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='EDA_17414513643700&#47;HistoricalGenreproduction' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ED&#47;EDA_17414513643700&#47;HistoricalGenreproduction&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1741455365311');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
"""

# Use Streamlit's HTML component to render it
st.components.v1.html(tableau_embed_code, width=900, height=1000, scrolling=True)
