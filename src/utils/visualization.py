"""Plotly visualizations for genuine, labeled NewsBot results."""
def topic_keywords_chart(modeler):
    import plotly.graph_objects as go
    fig=go.Figure()
    for i in range(modeler.n_topics):
        words=modeler.get_topic_words(i,8)
        fig.add_trace(go.Bar(name=f'Topic {i}',x=words,y=list(range(len(words),0,-1))))
    fig.update_layout(title='Top words per discovered topic',barmode='group')
    return fig
