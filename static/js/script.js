/* =========================================================
   ADITYA COLLEGE ERP
   MAIN JAVASCRIPT
   ========================================================= */


/* =========================================================
   GENERIC API REQUEST
   ========================================================= */

async function sendRequest(url, data) {

    try {

        const response = await fetch(url, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });


        const result = await response.json();

        return result;

    }

    catch (error) {

        console.error("Request error:", error);

        return {

            success: false,

            message: "Unable to connect to the server."

        };

    }

}


/* =========================================================
   NOTICE ICON
   ========================================================= */

function getNoticeIcon(title) {

    if (!title) {
        return "📢";
    }


    const text = title.toLowerCase();


    if (
        text.includes("exam") ||
        text.includes("examination")
    ) {

        return "📝";

    }


    if (
        text.includes("fee") ||
        text.includes("payment")
    ) {

        return "₹";

    }


    if (
        text.includes("result") ||
        text.includes("results")
    ) {

        return "★";

    }


    if (
        text.includes("calendar") ||
        text.includes("academic")
    ) {

        return "📅";

    }


    if (
        text.includes("holiday")
    ) {

        return "☀";

    }


    if (
        text.includes("notice") ||
        text.includes("announcement")
    ) {

        return "📢";

    }


    return "📢";

}


/* =========================================================
   NOTICE DATE
   ========================================================= */

function formatNoticeDate(dateValue) {

    if (!dateValue) {

        return {
            day: "--",
            month: ""
        };

    }


    const date = new Date(dateValue);


    if (isNaN(date.getTime())) {

        return {
            day: "--",
            month: ""
        };

    }


    const day =
        String(date.getDate()).padStart(2, "0");


    const month =
        date.toLocaleString(
            "en-US",
            {
                month: "short"
            }
        );


    return {
        day: day,
        month: month
    };

}


/* =========================================================
   LOAD NOTICES
   ========================================================= */

async function loadNotices() {

    const noticesContainer =
        document.getElementById("noticesContainer");

    if (!noticesContainer) {
        return;
    }


    noticesContainer.innerHTML =
        '<div class="loading">Loading notices...</div>';


    try {

        const response =
            await fetch("/api/notices");


        const notices =
            await response.json();


        if (!response.ok || !Array.isArray(notices)) {

            throw new Error("Failed to load notices");

        }


        if (notices.length === 0) {

            noticesContainer.innerHTML = `
                <div class="message">
                    No notices available.
                </div>
            `;

            return;
        }


        noticesContainer.innerHTML = "";


        notices.forEach(function (notice) {

            let date = new Date(notice.notice_date);


            let day =
                date.getDate();


            let month =
                date.toLocaleString(
                    "en-US",
                    {
                        month: "short"
                    }
                );


            let fullDate =
                notice.notice_date || "";


            const noticeCard =
                document.createElement("div");


            noticeCard.className =
                "notice-card";


            noticeCard.innerHTML = `

                <div class="notice-date-box">

                    <span class="notice-day">
                        ${day}
                    </span>

                    <span class="notice-month">
                        ${month}
                    </span>

                </div>


                <div class="notice-content">

                    <h3>
                        ${notice.title || ""}
                    </h3>

                    <p>
                        ${notice.description || ""}
                    </p>

                    <span class="notice-full-date">
                        ${fullDate}
                    </span>

                </div>

            `;


            noticesContainer.appendChild(
                noticeCard
            );

        });


    } catch (error) {

        console.error(
            "Notice loading error:",
            error
        );


        noticesContainer.innerHTML = `

            <div class="message error">
                Unable to load notices.
            </div>

        `;

    }

}


/* =========================================================
   ATTENDANCE
   ========================================================= */

const attendanceForm =
    document.getElementById(
        "attendanceForm"
    );


if (attendanceForm) {

    attendanceForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const studentInput =
                document.getElementById(
                    "studentId"
                );


            const resultContainer =
                document.getElementById(
                    "attendanceResult"
                );


            const studentId =
                studentInput.value.trim();


            if (!studentId) {

                resultContainer.innerHTML = `

                    <div class="message error">
                        Student ID is required.
                    </div>

                `;

                return;

            }


            resultContainer.innerHTML = `

                <div class="loading">
                    Loading attendance...
                </div>

            `;


            const result =
                await sendRequest(
                    "/api/attendance",
                    {
                        student_id: studentId
                    }
                );


            if (!result.success) {

                resultContainer.innerHTML = `

                    <div class="message error">
                        ${result.message ||
                        "Unable to fetch attendance."}
                    </div>

                `;

                return;

            }


            if (
                !result.data ||
                result.data.length === 0
            ) {

                resultContainer.innerHTML = `

                    <div class="message error">

                        No attendance records found
                        for Student ID:
                        <strong>${studentId}</strong>

                    </div>

                `;

                return;

            }


            let table = `

                <div class="attendance-results">

                    <h2>
                        Attendance Details
                    </h2>

                    <div class="attendance-table-container">

                        <table class="attendance-table">

                            <thead>

                                <tr>

                                    <th>
                                        Course
                                    </th>

                                    <th>
                                        Attended
                                    </th>

                                    <th>
                                        Total Classes
                                    </th>

                                    <th>
                                        Attendance
                                    </th>

                                </tr>

                            </thead>

                            <tbody>

            `;


            result.data.forEach(function(item) {

                table += `

                    <tr>

                        <td>
                            ${item.course}
                        </td>

                        <td>
                            ${item.attended}
                        </td>

                        <td>
                            ${item.total}
                        </td>

                        <td>
                            <strong>
                                ${item.percentage}%
                            </strong>
                        </td>

                    </tr>

                `;

            });


            table += `

                            </tbody>

                        </table>

                    </div>

                </div>

            `;


            resultContainer.innerHTML =
                table;

        }
    );

}


/* =========================================================
   FEES
   ========================================================= */

const feesForm =
    document.getElementById(
        "feesForm"
    );


if (feesForm) {

    feesForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const studentId =
                document.getElementById(
                    "studentId"
                ).value.trim();


            const resultContainer =
                document.getElementById(
                    "feesResult"
                );


            resultContainer.innerHTML = `

                <div class="loading">
                    Loading fee details...
                </div>

            `;


            const result =
                await sendRequest(
                    "/api/fees",
                    {
                        student_id: studentId
                    }
                );


            if (!result.success) {

                resultContainer.innerHTML = `

                    <div class="message error">
                        ${result.message ||
                        "Unable to fetch fee details."}
                    </div>

                `;

                return;

            }


            if (!result.data) {

                resultContainer.innerHTML = `

                    <div class="message error">
                        No fee record found.
                    </div>

                `;

                return;

            }


            const fee =
                result.data;


            resultContainer.innerHTML = `

                <div class="fee-grid">


                    <div class="fee-card">

                        <h3>
                            Total Fee
                        </h3>

                        <p>
                            ₹${fee.total}
                        </p>

                    </div>


                    <div class="fee-card">

                        <h3>
                            Paid Fee
                        </h3>

                        <p>
                            ₹${fee.paid}
                        </p>

                    </div>


                    <div class="fee-card">

                        <h3>
                            Pending Fee
                        </h3>

                        <p>
                            ₹${fee.pending}
                        </p>

                    </div>


                    <div class="fee-card">

                        <h3>
                            Status
                        </h3>

                        <p>
                            ${fee.status}
                        </p>

                    </div>


                </div>

            `;

        }
    );

}


/* =========================================================
   PAYMENT
   ========================================================= */

function proceedToPayment() {

    alert(
        "Payment gateway integration will be added later."
    );

}


/* =========================================================
   RESULTS
   =========================================================
   
   Results are intentionally NOT loaded on the public home page.
   
   They remain available through the authenticated dashboard.
   ========================================================= */


/* =========================================================
   LOGIN
   ========================================================= */

const loginForm =
    document.getElementById(
        "loginForm"
    );


if (loginForm) {

    loginForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            const username =
                document.getElementById(
                    "username"
                ).value.trim();


            const password =
                document.getElementById(
                    "password"
                ).value;


            const message =
                document.getElementById(
                    "loginMessage"
                );


            message.innerHTML = `

                <div class="loading">
                    Logging in...
                </div>

            `;


            const result =
                await sendRequest(
                    "/api/login",
                    {
                        username: username,
                        password: password
                    }
                );


            if (!result.success) {

                message.innerHTML = `

                    <div class="message error">

                        ${result.message ||
                        "Invalid login details."}

                    </div>

                `;

                return;

            }


            message.innerHTML = `

                <div class="message success">
                    Login successful.
                </div>

            `;


            /*
             * Send every successful login to the
             * existing dashboard route.
             *
             * The dashboard already checks the
             * session on the Flask side.
             */

            setTimeout(function() {

                window.location.href =
                    "/dashboard";

            }, 500);

        }
    );

}


/* =========================================================
   PAGE LOAD
   ========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function() {

        loadNotices();

    }
);