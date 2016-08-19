package shakar.smsapp;

import android.app.Activity;
import android.app.Dialog;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.telephony.SmsManager;
import android.text.method.ScrollingMovementMethod;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        final EditText et_number= (EditText) findViewById(R.id.numberofsms);
        final EditText et_sms= (EditText) findViewById(R.id.textsms);



       FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        assert fab != null;
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int number=Integer.valueOf(et_number.getText().toString());
                String text=et_sms.getText().toString();
                Dialog dialog=new Dialog(MainActivity.this);
                dialog.setContentView(R.layout.dialog_text);
                TextView senttext= (TextView) dialog.findViewById(R.id.logmessages);
                senttext.setMovementMethod(new ScrollingMovementMethod());

                String[] initial={"9803","9808","9806"};
                String finals;
                Random rand = new Random();
                for (int j=0;j<number;j++){
                    int  n = rand.nextInt(3);
                    finals=initial[n];
                    int later=100000 +rand.nextInt(900000);
                    sendSMS(finals+later,text,senttext);

                }
                dialog.show();

            }
        });
    }
    //---sends an SMS message to another device---
    private void sendSMS(final String phoneNumber, String message, final TextView senttext)
    {
        String SENT = "SMS_SENT";
        String DELIVERED = "SMS_DELIVERED";

        final PendingIntent sentPI = PendingIntent.getBroadcast(this, 0,
                new Intent(SENT), 0);

        PendingIntent deliveredPI = PendingIntent.getBroadcast(this, 0,
                new Intent(DELIVERED), 0);

        //---when the SMS has been sent---
        registerReceiver(new BroadcastReceiver(){
            @Override
            public void onReceive(Context arg0, Intent arg1) {
                switch (getResultCode())
                {
                    case Activity.RESULT_OK:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"Sent");
                        break;
                    case SmsManager.RESULT_ERROR_GENERIC_FAILURE:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"Generic Failure");
                        break;
                    case SmsManager.RESULT_ERROR_NO_SERVICE:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"No service");
                        break;
                    case SmsManager.RESULT_ERROR_NULL_PDU:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"No PDU");
                        break;
                    case SmsManager.RESULT_ERROR_RADIO_OFF:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"Radio off");
                        break;
                }
            }
        }, new IntentFilter(SENT));

        //---when the SMS has been delivered---
        registerReceiver(new BroadcastReceiver(){
            @Override
            public void onReceive(Context arg0, Intent arg1) {
                switch (getResultCode())
                {
                    case Activity.RESULT_OK:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"Delivered");
                        break;
                    case Activity.RESULT_CANCELED:
                        senttext.setText(senttext.getText()+"\n"+phoneNumber+": "+"Not delivered");
                        break;
                }
            }
        }, new IntentFilter(DELIVERED));

        SmsManager sms = SmsManager.getDefault();
        sms.sendTextMessage(phoneNumber, null, message, sentPI, deliveredPI);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
