import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def clean_data(df):
    """Clean the data"""
    # Remove rows where all values are NaN
    df = df.dropna(how='all')
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    return df

st.title("NBA Player Statistics Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload NBA Statistics CSV", type=['csv'])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Clean the data
    df = clean_data(df)
    
    st.success(f"✓ File uploaded successfully! Found {len(df)} rows.")
    
    # Show the first few rows
    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # Show basic info about the dataset
    st.subheader("Dataset Information")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Players", len(df))
        st.metric("Total Columns", len(df.columns))
    
    with col2:
        # Show column names
        st.write("**Available Columns:**")
        st.write(list(df.columns))

    # Sidebar for filters and options
    st.sidebar.header("Analysis Options")
    
    # Get numeric columns only (exclude Player, Pos, Tm)
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    # Select metric to analyze
    selected_metric = st.sidebar.selectbox(
        "Select Metric to Analyze",
        numeric_columns
    )
    
    # Number of top players to show
    top_n = st.sidebar.slider(
        "Number of Top Players",
        min_value=5,
        max_value=50,
        value=10
    )
    
    # Minimum games filter
    min_games = st.sidebar.number_input(
        "Minimum Games Played",
        min_value=0,
        max_value=82,
        value=20
    )

    # Multi-select for additional columns to display
    st.sidebar.subheader("Display Options")
    
    available_columns = [col for col in df.columns if col not in ['Player', 'Pos', 'Tm', 'G']]
    
    additional_columns = st.sidebar.multiselect(
        "Select Additional Columns to Display",
        options=available_columns,
        default=[selected_metric]
    )

    # Team filter
    st.sidebar.subheader("Filters")
    
    # Get unique teams
    all_teams = ['All Teams'] + sorted(df['Tm'].unique().tolist())
    
    selected_team = st.sidebar.selectbox(
        "Filter by Team",
        all_teams
    )

    # Position filter
    all_positions = ['All Positions'] + sorted(df['Pos'].unique().tolist())
    
    selected_position = st.sidebar.selectbox(
        "Filter by Position",
        all_positions
    )

    # Filter by minimum games
    filtered_df = df[df['G'] >= min_games].copy()
    
    # Filter by team if selected
    if selected_team != 'All Teams':
        filtered_df = filtered_df[filtered_df['Tm'] == selected_team]
    
    # Filter by position if selected
    if selected_position != 'All Positions':
        filtered_df = filtered_df[filtered_df['Pos'] == selected_position]

    # Sort by selected metric (descending - highest first)
    sorted_df = filtered_df.sort_values(by=selected_metric, ascending=False)
    
    # Get top N players
    top_players = sorted_df.head(top_n)
    
    # Display results
    st.subheader(f"Top {top_n} Players by {selected_metric}")
    st.write(f"(Filtered: Minimum {min_games} games played)")

    # Show summary statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Players Analyzed", len(filtered_df))
    with col2:
        st.metric("Average " + selected_metric, f"{filtered_df[selected_metric].mean():.2f}")
    with col3:
        st.metric("Highest " + selected_metric, f"{filtered_df[selected_metric].max():.2f}")
    
    # Bar chart of top players
    st.subheader(f"Visual Comparison: {selected_metric}")
    
    # Create chart data
    chart_data = top_players[['Player', selected_metric]].copy()
    chart_data = chart_data.set_index('Player')
    
    st.bar_chart(chart_data)

    # Distribution histogram
    st.subheader(f"Distribution of {selected_metric} (All Qualified Players)")
    
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(filtered_df[selected_metric].dropna(), bins=20, color='steelblue', edgecolor='black')
    ax.set_xlabel(selected_metric)
    ax.set_ylabel('Number of Players')
    ax.set_title(f'Distribution of {selected_metric}')
    
    st.pyplot(fig)

    # Show the ranked table with user-selected columns
    columns_to_show = ['Player', 'Pos', 'Tm', 'G']
    
    # Add user-selected additional columns
    for col in additional_columns:
        if col not in columns_to_show:
            columns_to_show.append(col)
    
    # Make sure selected_metric is included
    if selected_metric not in columns_to_show:
        columns_to_show.append(selected_metric)
    
    # Add rank column
    top_players_display = top_players[columns_to_show].copy()
    top_players_display.insert(0, 'Rank', range(1, len(top_players_display) + 1))
    
    st.dataframe(
        top_players_display,
        use_container_width=True,
        hide_index=True
    )

    # Download button for results
    csv = top_players_display.to_csv(index=False)
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name=f"top_{top_n}_players_by_{selected_metric}.csv",
        mime="text/csv"
    )

    # Player Comparison Section
    st.divider()
    st.header("🔍 Compare Two Players")
    
    col1, col2 = st.columns(2)
    
    with col1:
        player1 = st.selectbox(
            "Select First Player",
            df['Player'].unique(),
            key='player1'
        )
    
    with col2:
        player2 = st.selectbox(
            "Select Second Player",
            df['Player'].unique(),
            key='player2'
        )
    
    if st.button("Compare Players"):
        # Get player data
        p1_data = df[df['Player'] == player1].iloc[0]
        p2_data = df[df['Player'] == player2].iloc[0]
        
        # Display comparison
        st.subheader(f"{player1} vs {player2}")
        
        # Create comparison columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write(f"**{player1}**")
        with col2:
            st.write("**Stat**")
        with col3:
            st.write(f"**{player2}**")
        
        # Compare numeric stats
        for col in numeric_columns:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(col, f"{p1_data[col]:.2f}")
            with col2:
                st.write(col)
            with col3:
                st.metric(col, f"{p2_data[col]:.2f}")

else:
    st.info("👆 Upload a CSV file to get started")