import TimeAgo from 'javascript-time-ago'
import en from 'javascript-time-ago/locale/en'
TimeAgo.addDefaultLocale(en)

// Create formatter (English).

export default function phoneFormat(input) {

    if (!input || isNaN(input)) return `input must be a number was sent ${input}`
    if (typeof (input) !== 'string') input = input.toString()
    if (input.length === 10) {
        return input.replace(/(\d{3})(\d{3})(\d{4})/, "$1-$2-$3");
    } else {
        return 'N/A'
    }
}

export function timeDifference(time) {

    const date = new Date(time);
    var delta = Math.round((+new Date - date) / 1000);

    var minute = 60,
        hour = minute * 60,
        day = hour * 24,
        week = day * 7;
    
    var fuzzy;
    
    if (delta < 30) {
        fuzzy = 'just then.';
    } else if (delta < minute) {
        fuzzy = delta + ' seconds ago.';
    } else if (delta < 2 * minute) {
        fuzzy = 'a minute ago.'
    } else if (delta < hour) {
        fuzzy = Math.floor(delta / minute) + ' minutes ago.';
    } else if (Math.floor(delta / hour) == 1) {
        fuzzy = '1 hour ago.'
    } else if (delta < day) {
        fuzzy = Math.floor(delta / hour) + ' hours ago.';
    } else if (delta < day * 2) {
        fuzzy = 'yesterday';
    }

    return fuzzy;

}