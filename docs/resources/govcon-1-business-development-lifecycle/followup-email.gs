// ===================== FOLLOW-UP EMAIL (GovCon Session 1) =====================
// Sends each person who submits the worksheet a branded email with their own answers,
// today's links, and (if the file IDs below are filled in) the capture template and deck attached.
// Setup, once: run installTrigger. Test: run sendTestEmail (sends only to you).
// If Gmail hiccups: run resendFailed.

// Paste Drive file IDs here (the long ID in the file's Drive URL). Blank = no attachment.
var TEMPLATE_FILE_ID = 'YOUR-DRIVE-FILE-ID';   // 2026-04-28-capture-management-template.xlsx
var DECK_FILE_ID = 'YOUR-DRIVE-FILE-ID';       // deck PDF
var REPLY_TO = 'you@yourorg.org';
var SIGNUP_URL = 'https://mdsbdc.ecenterdirect.com/signup';

function installTrigger() {
  var form = FormApp.getActiveForm();
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'onFormSubmit') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('onFormSubmit').forForm(form).onFormSubmit().create();
  Logger.log('Trigger installed. Every new submission now gets the follow-up email.');
}

function onFormSubmit(e) {
  sendFor_(e.response);
}

function sendFor_(response) {
  var a = answers_(response);
  var to = a['Your email'];
  if (!to) { Logger.log('No email on response ' + response.getId()); return; }
  try {
    var opts = { name: 'Your Name, Maryland SBDC', replyTo: REPLY_TO, htmlBody: html_(a) };
    var files = attachments_();
    if (files.length) opts.attachments = files;
    MailApp.sendEmail(to, 'Your Session 1 worksheet, the links, and what comes next', text_(a), opts);
    markFailed_(response.getId(), false);
    Logger.log('SENT ' + to);
  } catch (err) {
    markFailed_(response.getId(), true);
    Logger.log('FAILED ' + to + ': ' + err);
  }
}

function answers_(response) {
  var out = {};
  response.getItemResponses().forEach(function (ir) {
    var v = ir.getResponse();
    var t = ir.getItem().getType();
    if (t === FormApp.ItemType.GRID) {
      var rows = ir.getItem().asGridItem().getRows();
      out['__grid'] = rows.map(function (r, i) { return [r, v[i] || '']; });
    } else {
      out[ir.getItem().getTitle()] = Array.isArray(v) ? v.join(', ') : v;
    }
  });
  return out;
}

function attachments_() {
  return [TEMPLATE_FILE_ID, DECK_FILE_ID].filter(String).map(function (id) {
    return DriveApp.getFileById(id).getBlob();
  });
}

function markFailed_(id, failed) {
  var p = PropertiesService.getScriptProperties();
  var list = JSON.parse(p.getProperty('failed') || '[]').filter(function (x) { return x !== id; });
  if (failed) list.push(id);
  p.setProperty('failed', JSON.stringify(list));
}

function resendFailed() {
  var form = FormApp.getActiveForm();
  var ids = JSON.parse(PropertiesService.getScriptProperties().getProperty('failed') || '[]');
  ids.forEach(function (id) { sendFor_(form.getResponse(id)); });
  Logger.log('Retried ' + ids.length);
}

// Preview: the real email for the newest form response, sent only to you.
function sendLatestToMe() {
  var rs = FormApp.getActiveForm().getResponses();
  if (!rs.length) { Logger.log('No responses yet.'); return; }
  var a = answers_(rs[rs.length - 1]);
  var me = Session.getActiveUser().getEmail();
  var opts = { name: 'Your Name, Maryland SBDC', replyTo: REPLY_TO, htmlBody: html_(a) };
  var files = attachments_();
  if (files.length) opts.attachments = files;
  MailApp.sendEmail(me, '[PREVIEW] Your Session 1 worksheet, the links, and what comes next', text_(a), opts);
  Logger.log('Preview of ' + rs.length + ' response(s), newest from ' + a['Your email'] + ', sent to ' + me + ' with ' + files.length + ' attachment(s).');
}

function sendTestEmail() {
  var me = Session.getActiveUser().getEmail();
  var a = {
    'Your name': 'Test Person', 'Your email': me, 'Business name': 'Example Facilities LLC',
    'Which revenue strategy are you running right now?': 'Strategy 1: sub under a small business',
    'One agency or buyer you would focus on first': 'Maryland Department of General Services',
    'One opportunity you are watching': 'Janitorial services, Anne Arundel County',
    '__grid': [['Customer: do you know them?', '2'], ['Competition: who else is bidding?', '2'],
               ['Capabilities: past performance on this work?', '4'], ['Cost: can you win on price?', '3']],
    'Your call today': 'Need more information',
    'The one capture step I will take this month': 'Register on eMMA and set alerts for my NAICS.',
    'Would you like free one-on-one advising from a Maryland SBDC consultant?': 'Yes, send me the sign-up link'
  };
  var opts = { name: 'Your Name, Maryland SBDC', replyTo: REPLY_TO, htmlBody: html_(a) };
  var files = attachments_();
  if (files.length) opts.attachments = files;
  MailApp.sendEmail(me, '[TEST] Your Session 1 worksheet, the links, and what comes next', text_(a), opts);
  Logger.log('Test sent to ' + me + ' with ' + files.length + ' attachment(s).');
}

// ----------------------------- content -----------------------------

var LINKS = [
  ['SAM.gov', 'https://sam.gov', 'Federal opportunities and your entity registration'],
  ['eMaryland Marketplace Advantage (eMMA)', 'https://emma.maryland.gov', 'Maryland state procurements, $30k+'],
  ['Acquisition Gateway forecasts', 'https://acquisitiongateway.gov/forecast', 'What federal agencies plan to buy next'],
  ['SBA Dynamic Small Business Search', 'https://search.certifications.sba.gov', 'How primes find small subs (keep your profile current)'],
  ['SBA certifications', 'https://certify.sba.gov', '8(a), WOSB/EDWOSB, HUBZone, VOSB/SDVOSB']
];

function first_(a) { return String(a['Your name'] || '').trim().split(/\s+/)[0] || 'there'; }
function esc_(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

function weakCount_(a) {
  return (a['__grid'] || []).filter(function (r) { return r[1] && Number(r[1]) < 3; }).length;
}

function html_(a) {
  var blue = '#002d62', red = '#d11142', ink = '#313438', mute = '#6a6d71', line = '#e2e4e7';
  var row = function (k, v) {
    return v ? '<tr><td style="padding:10px 0;border-top:1px solid ' + line + ';color:' + mute + ';font-size:13px;width:38%;vertical-align:top">' + esc_(k) +
      '</td><td style="padding:10px 0;border-top:1px solid ' + line + ';color:' + ink + ';font-size:15px">' + esc_(v) + '</td></tr>' : '';
  };
  var grid = (a['__grid'] || []).map(function (r) { return row(r[0], r[1] ? r[1] + ' / 5' : ''); }).join('');
  var weak = weakCount_(a);
  var flag = weak >= 2 ? '<p style="margin:14px 0 0;padding:12px 14px;background:#fceef2;border-left:4px solid ' + red + ';font-size:14px;color:' + ink +
    '">You scored ' + weak + ' of the Four C\'s below 3. That is the red-flag zone we talked about. Worth a conversation before you spend 150 hours on it.</p>' : '';
  var links = LINKS.map(function (l) {
    return '<li style="margin:0 0 10px"><a href="' + l[1] + '" style="color:' + red + ';font-weight:bold">' + esc_(l[0]) + '</a><br><span style="color:' + mute + ';font-size:13px">' + esc_(l[2]) + '</span></li>';
  }).join('');
  var wantsAdvising = /^Yes/.test(a['Would you like free one-on-one advising from a Maryland SBDC consultant?'] || '');
  var advising = wantsAdvising
    ? '<p style="margin:0 0 8px;font-size:15px;color:' + ink + '">You asked for free one-on-one advising. Register here and we will match you with a consultant:</p>' +
      '<p style="margin:0 0 4px"><a href="' + SIGNUP_URL + '" style="display:inline-block;background:' + red + ';color:#fff;text-decoration:none;font-weight:bold;padding:12px 20px">Register for advising</a></p>'
    : '<p style="margin:0;font-size:15px;color:' + ink + '">Free, confidential one-on-one advising is always open: <a href="' + SIGNUP_URL + '" style="color:' + red + '">' + SIGNUP_URL.replace('https://', '') + '</a></p>';
  var attached = [TEMPLATE_FILE_ID ? 'the capture management template' : '', DECK_FILE_ID ? 'today\'s slides' : ''].filter(String);
  var attachLine = attached.length ? '<p style="margin:0 0 18px;font-size:15px;color:' + ink + '">Attached: ' + attached.join(' and ') + '. Drop them into NotebookLM or ChatGPT and ask it questions.</p>' : '';

  return '<div style="background:#f4f6f8;padding:24px 12px;font-family:Arial,Helvetica,sans-serif">' +
    '<div style="max-width:600px;margin:0 auto;background:#fff">' +
    '<div style="background:' + blue + ';padding:22px 28px"><span style="display:inline-block;background:' + red + ';color:#fff;font-weight:bold;font-size:12px;letter-spacing:2px;padding:5px 10px">MARYLAND SBDC</span>' +
    '<div style="color:#fff;font-size:24px;font-weight:bold;margin-top:14px">Business Development Lifecycle</div>' +
    '<div style="color:#b8c8dd;font-size:13px;margin-top:4px">Winning That Government Contracting Award &middot; Session 1 &middot; Sept 28, 2026</div></div>' +
    '<div style="padding:26px 28px">' +
    '<p style="margin:0 0 14px;font-size:16px;color:' + ink + '">Thanks for joining today, ' + esc_(first_(a)) + '. Here is what you wrote, so you can act on it this week.</p>' +
    attachLine +
    '<div style="font-size:12px;font-weight:bold;letter-spacing:1.5px;color:' + red + ';margin:22px 0 4px">YOUR WORKSHEET</div>' +
    '<table style="width:100%;border-collapse:collapse">' +
    row('Your strategy', a['Which revenue strategy are you running right now?']) +
    row('First buyer to focus on', a['One agency or buyer you would focus on first']) +
    row('Opportunity you scored', a['One opportunity you are watching']) + grid +
    row('Your call', a['Your call today']) +
    row('Your one capture step this month', a['The one capture step I will take this month']) +
    '</table>' + flag +
    '<div style="font-size:12px;font-weight:bold;letter-spacing:1.5px;color:' + red + ';margin:26px 0 10px">WHERE TO LOOK</div>' +
    '<ul style="margin:0;padding-left:18px;font-size:15px">' + links +
    '<li style="margin:0"><b>Your county and city</b><br><span style="color:' + mute + ';font-size:13px">Search "[your county] procurement bid opportunities". Local buys start around $15k.</span></li></ul>' +
    '<div style="font-size:12px;font-weight:bold;letter-spacing:1.5px;color:' + red + ';margin:26px 0 10px">NEXT</div>' +
    '<p style="margin:0 0 14px;font-size:15px;color:' + ink + '"><b>Session 2: Team Roles and Responsibilities</b>, Wednesday, Sept 30, 10:00 a.m., same Zoom series.</p>' +
    advising +
    '<p style="margin:22px 0 0;font-size:15px;color:' + ink + '">Questions? Just reply to this email.<br>Your Name, Maryland SBDC</p>' +
    '</div>' +
    '<div style="padding:16px 28px;border-top:1px solid ' + line + ';color:' + mute + ';font-size:11px;line-height:1.5">Funded in part through a Cooperative Agreement with the U.S. Small Business Administration. All opinions, conclusions, and/or recommendations expressed herein are those of the author(s) and do not necessarily reflect the views of the SBA.</div>' +
    '</div></div>';
}

function text_(a) {
  var lines = ['Thanks for joining today, ' + first_(a) + '.', '', 'YOUR WORKSHEET',
    'Strategy: ' + (a['Which revenue strategy are you running right now?'] || ''),
    'First buyer: ' + (a['One agency or buyer you would focus on first'] || ''),
    'Opportunity: ' + (a['One opportunity you are watching'] || '')];
  (a['__grid'] || []).forEach(function (r) { lines.push(r[0] + ' ' + (r[1] || '-') + '/5'); });
  lines.push('Your call: ' + (a['Your call today'] || ''), 'Your one step: ' + (a['The one capture step I will take this month'] || ''), '', 'WHERE TO LOOK');
  LINKS.forEach(function (l) { lines.push(l[0] + ': ' + l[1]); });
  lines.push('', 'NEXT: Session 2, Team Roles and Responsibilities, Wed Sept 30, 10:00 a.m.',
    'Free one-on-one advising: ' + SIGNUP_URL, '', 'Your Name, Maryland SBDC');
  return lines.join('\n');
}
