import streamlit as st

st.title("American Airlines Calculator")

tabs = ["Miles vs Purchase", "Basic Economy vs Main Cabin", "Road to Status"]
tab1, tab2, tab3 = st.tabs(tabs)

with tab1:
    st.header("🎟️ Miles vs. Purchase Comparison")

    # Create two side-by-side containers for inputs
    col1, col2 = st.columns(2)

    # Flight purchase with miles inputs
    with col1:
        st.subheader("✈️ Flight with Miles")
        miles_required = st.number_input("Miles Required:", min_value=0, step=1000, format="%d")
        fees = st.number_input("Award Ticket Fees ($):", min_value=0.0, step=5.0, format="%.2f")

    # Flight purchase with cash input
    with col2:
        st.subheader("💰 Flight with Cash")
        cash_price = st.number_input("Cash Price ($):", min_value=0.0, step=10.0, format="%.2f")

    # Average value of AA miles in cents
    mile_value = 1.6  # This can be adjusted based on latest valuations

    # Calculate button
    if st.button("🔍 Compare Options"):
        # Calculate the equivalent dollar value of miles
        miles_value_dollars = (miles_required * mile_value) / 100

        # Total cost for miles redemption
        total_miles_cost = miles_value_dollars + fees

        # Determine the better option
        if total_miles_cost < cash_price:
            recommendation = "✅ Redeeming miles is the better deal!"
            color = "success"
        else:
            recommendation = "⚠️ Paying cash is the better deal!"
            color = "warning"

        # Output section
        with st.container():
            st.markdown(f"### ✨ **Results** ✨")
            st.markdown("---")  # Divider for a clean look

            col1, col2 = st.columns(2)

            with col1:
                st.metric(label="🎯 **Miles Value (in $)**", value=f"${miles_value_dollars:.2f}")
                st.metric(label="💳 **Total Cost Using Miles**", value=f"${total_miles_cost:.2f}")

            with col2:
                st.metric(label="💵 **Cash Price of Flight**", value=f"${cash_price:.2f}")

            # Display recommendation with color-coded message
            st.markdown("---")
            st.markdown(f"### 🏆 **Final Verdict**")
            st.write(f"💡 {recommendation}")
            if color == "success":
                st.success(recommendation)
            else:
                st.warning(recommendation)

import streamlit as st

# Define the benefits and earning rates for each status level
status_benefits = {
    "Gold": {
        "bonus_multiplier": 0.40,
        "upgrade_window": "24 hours",
        "free_checked_bags": 1,
        "oneworld_status": "Ruby",
        "priority_group": 4
    },
    "Platinum": {
        "bonus_multiplier": 0.60,
        "upgrade_window": "48 hours",
        "free_checked_bags": 2,
        "oneworld_status": "Sapphire",
        "priority_group": 3
    },
    "Platinum Pro": {
        "bonus_multiplier": 0.80,
        "upgrade_window": "72 hours",
        "free_checked_bags": 3,
        "oneworld_status": "Emerald",
        "priority_group": 2
    },
    "Executive Platinum": {
        "bonus_multiplier": 1.20,
        "upgrade_window": "100 hours",
        "free_checked_bags": 3,
        "oneworld_status": "Emerald",
        "priority_group": 1
    }
}

# Average value of AA miles (in cents)
mile_value = 1.6  # This value can be adjusted based on current valuations

with tab2:
    st.header("🛫 Basic Economy vs. Main Cabin Comparison")

    # Status selection
    status = st.selectbox("Select your AAdvantage® Status:", options=list(status_benefits.keys()))

    # Retrieve benefits for the selected status
    benefits = status_benefits[status]
    bonus_multiplier = benefits["bonus_multiplier"]

    # Create two side-by-side containers for inputs
    col1, col2 = st.columns(2)

    # Basic Economy input
    with col1:
        st.subheader("Basic Economy")
        basic_economy_price = st.number_input("Basic Economy Price ($):", min_value=0.0, step=10.0, format="%.2f")

    # Main Cabin input
    with col2:
        st.subheader("Main Cabin")
        main_cabin_price = st.number_input("Main Cabin Price ($):", min_value=0.0, step=10.0, format="%.2f")

    # Calculate button
    if st.button("Compare Fares"):
        # Calculate miles earned
        basic_economy_miles = basic_economy_price * (2 + 2 * bonus_multiplier)
        main_cabin_miles = main_cabin_price * (5 + 5 * bonus_multiplier)

        # Calculate price difference
        price_difference = main_cabin_price - basic_economy_price

        # Calculate additional miles value
        additional_miles = main_cabin_miles - basic_economy_miles
        additional_miles_value = (additional_miles * mile_value) / 100

        # Adjusted price difference considering miles value
        adjusted_price_difference = price_difference - additional_miles_value

        # Display results
        st.markdown("### ✨ **Comparison Results** ✨")
        st.markdown("---")  # Divider for a clean look

        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="**Miles Earned with Basic Economy**", value=f"{basic_economy_miles:.2f} miles")
            st.metric(label="**Miles Earned with Main Cabin**", value=f"{main_cabin_miles:.2f} miles")
            st.metric(label="**Price Difference**", value=f"${price_difference:.2f}")

        with col2:
            st.metric(label="**Additional Miles Value**", value=f"${additional_miles_value:.2f}")
            st.metric(label="**Adjusted Price Difference**", value=f"${adjusted_price_difference:.2f}")

        # Display additional benefits for Main Cabin
        st.markdown("---")
        st.markdown("### 🛋️ **Main Cabin Additional Benefits**")
        st.write(f"- **Free Checked Bags:** {benefits['free_checked_bags']}")
        st.write(f"- **Upgrade Window:** {benefits['upgrade_window']} before departure")
        st.write(f"- **Priority Boarding Group:** Group {benefits['priority_group']}")
        st.write(f"- **Oneworld Status:** {benefits['oneworld_status']}")

        # Recommendation
        st.markdown("---")
        st.markdown("### 🏆 **Recommendation**")
        if adjusted_price_difference > 0:
            st.warning("**Basic Economy is more cost-effective after considering miles earned.**")
        else:
            st.success("**Main Cabin is more cost-effective after considering miles earned and additional benefits.**")


with tab3:
    st.header("Road to Status")

    # User input for current Loyalty Points balance
    current_loyalty_points = st.number_input(
        "Enter your current Loyalty Points balance:",
        min_value=0,
        value=0,
        step=1000
    )

    # Select target elite status
    status_options = {
        "Gold": 40000,
        "Platinum": 75000,
        "Platinum Pro": 125000,
        "Executive Platinum": 200000
    }
    target_status = st.selectbox(
        "Select your target elite status:",
        options=list(status_options.keys())
    )
    target_points = status_options[target_status]

    # Calculate points needed to reach target status
    points_needed = max(target_points - current_loyalty_points, 0)
    st.write(f"**Loyalty Points needed to reach {target_status} status:** {points_needed}")

    if points_needed > 0:
        st.write("Adjust the sliders below to see how different spending strategies can help you achieve your target status.")

        # Slider for total credit card spending
        cc_spend = st.slider(
            "Total planned credit card spending ($):",
            min_value=0,
            max_value=100000,
            value=10000,
            step=1000
        )

        # Slider for total flight spending
        flight_spend = st.slider(
            "Total planned spending on Main Cabin flights ($):",
            min_value=0,
            max_value=100000,
            value=5000,
            step=1000
        )

        # Calculate Loyalty Points from each source
        cc_points = cc_spend * 1  # 1 LP per $1 spent
        flight_points = flight_spend * 7  # 7 LPs per $1 spent

        # Total Loyalty Points
        total_points = current_loyalty_points + cc_points + flight_points

        # Determine achieved status
        achieved_status = None
        for status, threshold in reversed(status_options.items()):
            if total_points >= threshold:
                achieved_status = status
                break

        # Display results
        st.write(f"**Total Loyalty Points after planned spending:** {total_points}")
        if achieved_status:
            st.write(f"**Congratulations! You've reached {achieved_status} status.**")
        else:
            st.write(f"**You have not reached a new status level.**")

        # Calculate and display adjusted monthly spend
        months_remaining = 12  # Assuming a 12-month qualification period
        adjusted_monthly_cc_spend = cc_spend / months_remaining
        adjusted_monthly_flight_spend = flight_spend / months_remaining
        st.write(f"**Adjusted Monthly Credit Card Spend:** ${adjusted_monthly_cc_spend:.2f}")
        st.write(f"**Adjusted Monthly Flight Spend:** ${adjusted_monthly_flight_spend:.2f}")
    else:
        st.write(f"Congratulations! You've already achieved {target_status} status.")
