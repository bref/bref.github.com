css = """\
"""

html = """\
<div class="container doc-exemple">
  {{#sources?}}
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  {{/sources?}}
  <header class="jumbotron subhead" id="overview">
    <h1>Exemple : {{ title }}</h1>
  </header>
  <div class='clearall example-wrapper'>
  <div class="background"></div>
  {{#sections}}
  <div class='row' id='section-{{ num }}'>
    <div class='span6 example-doc-text'>
      {{{ docs_html }}}&nbsp;
    </div>
    <div class='span6 example-doc-code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
"""
